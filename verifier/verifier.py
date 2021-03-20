import requests

PREFIXES = ('LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS')
ACTIONS = ('Added', 'Deleted', 'Fixed', 'Refactored', 'Moved')
GROUPS = ('1022', '1021')

TOKEN = ''


def prepare_headers():
    return {
        'Authorization': f'token {TOKEN}',
    }


def get_all_user_prs(user_login: str, repo_name: str):
    all_pr = requests.get(f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state=open',
                          headers=prepare_headers())
    return all_pr


def get_all_pr_not_reviewed_commits(pr):
    raw_commits = requests.get(pr['commits_url'], headers=prepare_headers()).json()
    # list of reviewed commits
    reviewed = set(list(map(lambda x: x['commit_id'],
                        requests.get(pr['review_comments_url'], headers=prepare_headers()).json()
                            )))
    raw_commits_no_reviewed = list(filter(lambda x: x['sha'] not in reviewed, raw_commits))
    nice_commits = list(map(lambda x: x['commit']['message'], raw_commits_no_reviewed))
    return nice_commits


def check_prefixes(title):
    message = ""
    title_splitted = title.split('-')
    pre = title_splitted[0]
    post = title_splitted[1].split(' ')
    if pre not in PREFIXES:
        message = f"{message}Prefix is not in {PREFIXES}\n"
    if post[0] not in GROUPS:
        message = f"{message}Group is not in {GROUPS}\n"
    if len(post) > 1 and post[1] not in ACTIONS:
        message = f"{message}Action is not in {ACTIONS}\n"
    return message


def create_review(pr):
    if check_prefixes(pr['title']):
        review = f"Your PR: {pr['title']}\n{check_prefixes(pr['title'])}\n"
    else:
        review = ""
    for commit_message in get_all_pr_not_reviewed_commits(pr):
        if len(check_prefixes(commit_message)) > 1:
            review = f'{review}Your commit: {commit_message}\n{check_prefixes(commit_message)}'
    return review


def send_pr_review(pr, message):
    if message == "":
        pass
    else:
        data = {
            'body': message,
            'path': requests.get(f"{pr['url']}/files", headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha'],
        }
        requests.post(f"{pr['url']}/comments", headers=prepare_headers(), json=data)


if __name__ == '__main__':
    # import json
    #
    # with open('test_pulls.json', 'w', encoding='utf-8') as f:
    #     json.dump(get_all_user_prs('dantatartes', 'test').json(), f, ensure_ascii=False, indent=4)
    for pull_request in get_all_user_prs('dantatartes', 'test').json():
        pr_review = create_review(pull_request)
        send_pr_review(pull_request, pr_review)
