import requests

PREFIXES = ('LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS')
ACTIONS = ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')
GROUPS = ('1022', '1021')

TOKEN = ''


def make_link(user_login, repo_names) -> str:
    return f'https://api.github.com/repos/{user_login}/{repo_names}/pulls?state=open'


def prepare_headers():
    return {
        'Autorization': f'token {TOKEN}',
        'Content-Type': "application/json",
        'Accept': "application/vnd.github.v3+json"
    }


def get_all_user_prs(user_login: str, repo_names: str):
    all_pr = requests.get(make_link(user_login, repo_names), headers=prepare_headers())
    return all_pr


def get_all_pr_commits(pr):
    raw_commits = requests.get(pr['commits_url'], headers=prepare_headers()).json()
    nice_commits = list(map(lambda x: (x['commit']['message']), raw_commits))
    return nice_commits


def check_prefixes(title):
    comments = []
    title_splitted = title.split('-')
    pre = title_splitted[0]
    post = title_splitted[1].split(' ')
    if pre not in PREFIXES:
        comments.append("Prefix is not in {}\n".format(PREFIXES))
    if post[0] not in GROUPS:
        comments.append("Group is not in {}\n".format(GROUPS))
    if len(post) > 1 and post[1] not in ACTIONS:
        comments.append(f"Action not in {ACTIONS}\n")
    return comments


def create_message(pr):
    message = f"Your PR: {pr['title']}\n{check_prefixes(pr['title'])}\n\n"
    for commit_message in get_all_pr_commits(pr):
        message = f'{message}Your commit: {commit_message}\n{check_prefixes(commit_message)}\n'
    return message


def send_pr_comment(pr, message):
    data = {'body': message,
            'path': requests.get(pr['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(f"{pr['url']}/comments", headers=prepare_headers(), json=data)
    print(r.json())


if __name__ == '__main__':
    for pull_request in get_all_user_prs('dantatartes', 'python_au').json():
        if create_message(pull_request):
            send_pr_comment(pull_request, create_message(pull_request))
