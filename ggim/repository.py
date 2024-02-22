import subprocess
import re
from networkx import DiGraph
from datetime import datetime, timezone, timedelta

from ggim import Commit


class Repository:
    def __init__(self, repo_path: str):
        self._path = repo_path
        self._commit_graph: DiGraph = DiGraph()
        self._init_commit_graph_from_git_repo()

    @property
    def head(self) -> Commit:
        return self._get_commit("HEAD")

    @property
    def number_of_commits(self) -> int:
        return self._commit_graph.number_of_nodes()

    def _init_commit_graph_from_git_repo(self) -> DiGraph:
        commits_to_explore = ["HEAD"]

        while commits_to_explore:
            current_commitish = commits_to_explore.pop(0)
            current_commit = self._get_commit(current_commitish)

            self._commit_graph.add_node(
                current_commit.commit_hash,
                tree_hash=current_commit.tree_hash,
                commit_time=current_commit.commit_time,
                committer=current_commit.committer,
                author_time=current_commit.author_time,
                author=current_commit.author,
                message=current_commit.message,
            )

            for parent_hash in current_commit.parent_hashes:
                self._commit_graph.add_node(parent_hash)
                self._commit_graph.add_edge(current_commit.commit_hash, parent_hash)
                commits_to_explore.append(parent_hash)

    def _get_commit_hash(self, commitish: str) -> str:
        return (
            subprocess.check_output(["git", "-C", self._path, "rev-parse", commitish])
            .decode("utf-8")
            .strip()
        )

    def _get_commit_content(self, commitish: str) -> str:
        return (
            subprocess.check_output(
                ["git", "-C", self._path, "cat-file", "-p", commitish]
            )
            .decode("utf-8")
            .removesuffix("\n")
        )

    def _get_commit(self, commitish: str) -> Commit:
        commit_hash = self._get_commit_hash(commitish)
        commit_content = self._get_commit_content(commitish).splitlines()

        tree_hash = commit_content.pop(0).removeprefix("tree ")

        parent_hashes = []
        while commit_content[0].startswith("parent "):
            parent_hashes.append(commit_content.pop(0).removeprefix("parent "))

        pattern = re.compile(
            "(?P<name>.* <.*>) (?P<timestamp>\d*) (?P<offset_sign>(?:\+|-))(?P<offset_hours>\d{2})(?P<offset_minutes>\d{2})"
        )

        authoring_info = pattern.search(commit_content.pop(0).removeprefix("author "))
        author = authoring_info.group("name")

        sign = -1 if authoring_info.group("offset_sign") == "-" else 1

        author_time = datetime.fromtimestamp(
            int(authoring_info.group("timestamp")),
            timezone(
                sign
                * timedelta(
                    hours=int(authoring_info.group("offset_hours")),
                    minutes=int(authoring_info.group("offset_minutes")),
                )
            ),
        )

        committing_info = pattern.search(
            commit_content.pop(0).removeprefix("committer ")
        )
        committer = committing_info.group("name")

        sign = -1 if committing_info.group("offset_sign") == "-" else 1

        committer_time = datetime.fromtimestamp(
            int(committing_info.group("timestamp")),
            timezone(
                sign
                * timedelta(
                    hours=int(committing_info.group("offset_hours")),
                    minutes=int(committing_info.group("offset_minutes")),
                )
            ),
        )

        commit_content.pop(0)

        message = "\n".join(commit_content)

        return Commit(
            commit_hash=commit_hash,
            parent_hashes=parent_hashes,
            tree_hash=tree_hash,
            commit_time=committer_time,
            committer=committer,
            author_time=author_time,
            author=author,
            message=message,
        )
