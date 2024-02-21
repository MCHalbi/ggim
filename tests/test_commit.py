import unittest
from ggim import Commit


class CommitTest(unittest.TestCase):
    def test_commit_has_commit_hash(self):
        commit = Commit("somelonghash")
        self.assertTrue(bool(commit.long_hash))
