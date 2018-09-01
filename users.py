import requests
import time

USER_NAME = 'ads'
USER_TOKEN = 'ads'

BASE_URL = 'https://api.github.com/'

def checkUserExists(username):
	userResponse = requests.get(BASE_URL + 'users/' + username, auth=(USER_NAME, USER_TOKEN))
	return (userResponse.status_code == 200)


def getReposOfUser(username):
	userRepos = []

	reposResponse = requests.get(BASE_URL + 'users/' + username + '/repos?per_page=2', auth=(USER_NAME, USER_TOKEN))
	print(reposResponse.headers['Link'])
	repos = reposResponse.json()
	for repo in repos:
		userRepos.append(repo['url'])

	return userRepos

# reposResponse = requests.get('https://api.github.com/repos/captn3m0/ifttt-webhook/stats/contributors', auth=(USER_NAME, USER_TOKEN))

# responseStatus = reposResponse.status_code

# if (responseStatus == 202):
# 	time.sleep(10)
# 	reposResponse = requests.get('https://api.github.com/repos/captn3m0/ifttt-webhook/stats/contributors', auth=(USER_NAME, USER_TOKEN))

# print (reposResponse.json())


# print(checkUserExists('captn3m0'))
userRepos = getReposOfUser('captn3m0')
print (userRepos)
