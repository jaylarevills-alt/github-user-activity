import requests

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        print(f"\nRecent activity for {username}:\n")
        for event in events[:5]:
            repo_name = event['repo']['name']
            event_type = event['type']
            print(f"Repo: {repo_name} | Event: {event_type}")
    elif response.status_code == 404:
        print("User not found. Please check the username.")
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
def get_top_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        sorted_repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)
        print(f"\nTop repositories for {username}:\n")
        for repo in sorted_repos[:5]:
            print(f"Repo: {repo['name']} | Stars: {repo['stargazers_count']}")
    elif response.status_code == 404:
        print("User not found. Please check the username.")
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code})")

if __name__ == "__main__":
    username = input("Enter a GitHub username: ")
    get_github_activity(username)
    get_top_repositories(username)
