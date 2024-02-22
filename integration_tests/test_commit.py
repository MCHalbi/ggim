import unittest
from ggim import Commit, Repository


class IntegrationTest(unittest.TestCase):
    def test_get_commit_from_a_repository(self):
        repository = Repository("./test_repository")
        commit = repository.head

        self.assertTrue(bool(commit.commit_hash))
