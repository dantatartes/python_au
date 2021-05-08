import requests
from datetime import datetime
import json
from typing import *

PREFIXES = ('LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS')
ACTIONS = ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')
GROUPS = ('1022', '1021')

TOKEN = ''


def prepare_headers() -> Dict[str, str]:
    return {
        'Authorization': f'token {TOKEN}',
    }


def prepare_body(pull: Dict[str, Any], comment: str) -> Dict[str, Union[str, int]]:
    return {
        'body': f"{comment}",
        'path': requests.get(f"{pull['url']}/files", headers=prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }


def get_all_user_prs(user_login: str, repo_name: str, pr_state: str) -> List[Dict[str, Any]]:
    url = f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state={pr_state}'
    prs = requests.get(url, headers=prepare_headers())
    return prs.json()


def get_all_pr_commits(pr: Dict[str, Any]) -> List[Dict[str, Any]]:
    return requests.get(pr['commits_url'], headers=prepare_headers()).json()


def check_prefixes(message: str) -> str:
    comment = []
    message_parts = message.split()
    prefix_parts = message_parts[0].split('-')
    if len(prefix_parts) == 1:
        prefix_parts.append('')
    elif len(prefix_parts) != 2:
        prefix_parts = ['', '']
    task, group = prefix_parts

    if task not in PREFIXES:
        comment.append(f"Message must start with code word in {PREFIXES}")

    if group not in GROUPS:
        comment.append(f"Message must contain group number in {GROUPS}")

    if len(message_parts) == 1 or message_parts[1] not in ACTIONS:
        comment.append(f"Message must start with {ACTIONS}")

    if len(comment) != 0:
        comment.insert(0, f"Invalid Commit Message: {message}")
        return '\n'.join(comment)
    return ''


def verify_pr(pr: Dict[str, Any]) -> None:
    comments = []
    all_commits = get_all_pr_commits(pr)
    for commit in all_commits:
        comment = check_prefixes(commit['commit']['message'])
        if len(comment) > 0:
            comments.append(comment)
    if len(comments) != 0:
        comments.insert(0, f"Invalid PULL Commits")
        send_pr_comment(pr, '\n\n'.join(comments))


def send_pr_comment(pull: Dict[str, Any], comment: str) -> str:
    url = f"{pull['url']}/comments"
    requests.post(url,
                  headers=prepare_headers(),
                  data=json.dumps(prepare_body(pull, comment)))
    return pull['html_url']


def str_to_date(date: str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")


def get_comment_by_date(pr: Dict[str, Any], author: str) -> Optional[datetime]:
    r = requests.get(pr['review_comments_url']).json()

    if len(r) > 0 and r[-1]['user']['login'] == author:
        return str_to_date(r[-1]['created_at'])
    return None


def get_commit_date(commit: Dict[str, Any]) -> datetime:
    return str_to_date(commit['commit']['author']['date'])


def check_new_commits(pr: Dict[str, Any], date: datetime) -> None:
    comments = list()
    all_commits = get_all_pr_commits(pr)
    for commit in all_commits:
        if get_commit_date(commit) > date:
            comment = check_prefixes(commit['commit']['message'])
            if len(comment) > 0:
                comments.append(comment)

    if len(comments) != 0:
        comments.insert(0, "VERIFICATION RESULT: ")
        send_pr_comment(pr, '\n\n'.join(comments))


if __name__ == '__main__':
    repo_name, state, reviewer = 'test', 'open', 'dantatartes'
    pulls = get_all_user_prs(user_login=reviewer, repo_name=repo_name, pr_state=state)
    for pr in pulls:
        comment_date = get_comment_by_date(pr, reviewer)
        if comment_date is not None:
            check_new_commits(pr, comment_date)
        else:
            verify_pr(pr)
