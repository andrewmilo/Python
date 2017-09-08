from github import Github
import sys

if len(sys.argv) < 2:
    sys.exit()

name = sys.argv[1]

with open( "info.txt" ) as f:
    lines = f.readlines()

username = lines[0].strip()
password = lines[1]

g = Github( username, password )

g.get_user().create_repo( name )