from celery import shared_task
import requests

@shared_task
def fetch_github_repos(username):
    user = requests.get(f'https://api.github.com/users/{username}/repos').json()
    result = []
    for reposit in user:
        info = {
            'name': reposit['name'],
            'url': reposit['html_url'],
            'stars': reposit['stargazers_count']
        }
        result.append(info)
    return result