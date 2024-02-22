import unittest
from datetime import datetime, timezone, timedelta
from ggim import Repository


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self._repository_path = "./test_repository"

    def test_repository_commit_count(self):
        repository = Repository(self._repository_path)

        self.assertEqual(repository.number_of_commits, 20)

    def test_get_current_head_from_repository(self):
        repository = Repository(self._repository_path)
        head = repository.head

        self.assertEqual(head.commit_hash, "9e4a753cf5817c0f8c92b4390d3a8c611e4ae6cf")
        self.assertEqual(head.tree_hash, "48a5dbbf5ff662373648080b81dd09c435457bdc")
        self.assertListEqual(
            head.parent_hashes,
            [
                "d9644056eb6317cbeafe5fd34ada6c2845379eca",
                "e59b3193beb54abab34e4608991cd00c7046db70",
            ],
        )
        self.assertEqual(head.author, "Lukas Halbritter <halbi93@gmx.de>")
        self.assertEqual(
            head.author_time,
            datetime(2024, 2, 16, 11, 14, 47, tzinfo=timezone(timedelta(hours=1))),
        )
        self.assertEqual(head.committer, "Lukas Halbritter <halbi93@gmx.de>")
        self.assertEqual(
            head.commit_time,
            datetime(2024, 2, 16, 11, 14, 47, tzinfo=timezone(timedelta(hours=1))),
        )
