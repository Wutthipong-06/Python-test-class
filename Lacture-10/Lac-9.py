import requests

response = requests.get('https://apt.github.com/users/octocat')

if response.status_code == 200:
    user_data = response.json()
    print(f'Username: {user_data['Login']}')
    print(f"Name: {user_data['name']}")
    print(f'Bio: {user_data['bio']}')
    print(f'Public Repos: {user_data['public_repos']}')
    print(f'Followers: {user_data['followers']}')
    print(f'Following: {user_data['following']}')
else:
    print('Failed to retrieve data.')