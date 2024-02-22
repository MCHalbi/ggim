from attrs import define
from datetime import datetime
from typing import List


@define
class Commit:
    commit_hash: str
    parent_hashes: List[str]
    tree_hash: str
    commit_time: datetime
    committer: str
    author_time: datetime
    author: str
    message: str
