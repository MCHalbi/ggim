import networkx
from ggim import Commit


class CommitGraph:
    def __init__(self):
        self._graph = networkx.DiGraph()

    def add_commit(self, commit: Commit):
        if not self._graph.has_node(commit.commit_hash):
            self._graph.add_node(
                commit.commit_hash,
                tree=commit.tree_hash,
                committer=commit.committer,
                commit_time=commit.commit_time,
                author=commit.author,
                author_time=commit.author_time,
                message=commit.message,
            )
