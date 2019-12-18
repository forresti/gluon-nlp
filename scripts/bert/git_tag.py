import subprocess
import argparse
import sys
from datetime import datetime as dt

def check_git_status():
    '''
    Fail if there are modified files that are tracked by git.
    Untracked files are fine.
    '''
    result_str = ""
    output = subprocess.check_output(["git", "status"])
    output = str(output)
    if ("Changes not staged for commit" in output) or ("Changes to be committed:" in output):
        print("You have modified tracked files in your repo. Cannot create git tag.")
        print(output)
        return False
    else:
        return True

def get_current_datetime():
    now = dt.now()
    return now.strftime('%Y-%m-%d_%H.%M.%S')

def commit_git_tag(tag_str):
    error_code = subprocess.call(f"git tag -a {tag_str} -m {tag_str}".split(' '))
    print(f"error code: {error_code}")
    if error_code != 0:
        return error_code

    error_code = subprocess.call(f"git push --tag".split(' '))
    return error_code
