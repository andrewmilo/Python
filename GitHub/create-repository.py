# Parameters = GitHub username, password, repository name

from github import Github
import sys

if len(sys.argv) < 4:
    sys.exit()

username = sys.argv[1]
pw = sys.argv[2]
name = sys.argv[3]

g = Github( username, pw )

g.get_user().create_repo( name )