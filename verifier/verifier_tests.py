import unittest
import json


from verifier import *

TOKEN = ''


class TestVerifierMethods(unittest.TestCase):
    def test_prepare_headers(self):
        self.assertEqual(prepare_headers(), {'Authorization': f'token {TOKEN}'})

    def test_get_all_user_prs(self):
        user_login, repo_name = 'dantatartes', 'test'
        with open('test_pulls.json') as f:
            prs = json.load(f)
            self.assertEqual(get_all_user_prs(user_login, repo_name).json(), prs)

    def test_get_all_pr_not_reviewed_commits(self):
        with open('test_pulls.json') as f:
            pr = json.load(f)[-1]
            commits = ["REQUESTS-1021 Added nice commit"]
            self.assertEqual(get_all_pr_not_reviewed_commits(pr), commits)

    def test_check_prefixes(self):
        title1 = "REQUESTS-1021 Added nice commit"
        title2 = "REQUESTS-1021 Another wrong added"
        message1 = ""
        message2 = "Action is not in ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')\n"
        self.assertEqual(check_prefixes(title1), message1)
        self.assertEqual(check_prefixes(title2), message2)

    def test_create_review(self):
        with open('test_pulls.json') as f:
            pr_bad_but_reviewed, pr_good_title_bad_commit, pr_bad, pr_good = json.load(f)
            review1 = ""
            review2 = "Your commit: REQUESTS-1021 Another wrong added\nAction is not in ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')\n"
            review3 = "Your PR: REQUESTS-1021 Wrong commit added!!!\nAction is not in ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')\n\nYour commit: REQUESTS-1021 Wrong commit added!!!\nAction is not in ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')\n"
            review4 = ""
            self.assertEqual(create_review(pr_bad_but_reviewed), review1)
            self.assertEqual(create_review(pr_good_title_bad_commit), review2)
            self.assertEqual(create_review(pr_bad), review3)
            self.assertEqual(create_review(pr_good), review4)

    def test_send_pr_review(self):
        pr_bad_but_reviewed = get_all_user_prs('dantatartes', 'test').json()[0]
        reviews_before = requests.get(pr_bad_but_reviewed['review_comments_url'], headers=prepare_headers()).json()
        send_pr_review(pr_bad_but_reviewed, create_review(pr_bad_but_reviewed))
        pr_bad_but_reviewed = get_all_user_prs('dantatartes', 'test').json()[0]
        reviews_after = requests.get(pr_bad_but_reviewed['review_comments_url'], headers=prepare_headers()).json()
        self.assertEqual(reviews_before, reviews_after)


if __name__ == '__main__':
    unittest.main()
