"""
==============================
WikiPages Auto-Installer
==============================

Just run this script, and it'll pull down the WikiPages repo for you.
It'll drop the files in these spots or a location of your choice:

- Linux: /var/www/wikipages
- Windows: C:\inetpub\wwwroot\wikipages

The first time you run it, the script will:
- Create and populate config file.
- Set up a fresh Git repo for the article pages.

Easy peasy!
"""

import os, platform, colorama
from colorama import Fore
from git import Repo
from git.exc import *

REPO_URL = 'https://github.com/itsdanjc/wiki-pages.git'
DEFAULT_INSTALL_LOCATIONS = {
    "Linux": r"/var/www/wikipages",
    "Windows": r"C:\inetpub\wwwroot\wikipages"
}

def clone() -> Repo | None: 
    # Replace with your repository URL
    curr_os = platform.system()
    install_location = DEFAULT_INSTALL_LOCATIONS[curr_os]
    if curr_os in DEFAULT_INSTALL_LOCATIONS:
        if input(f"Clone repo into {install_location}? ").lower() in {"", "y", "yes", "true"}:
            try:
                return Repo.clone_from(REPO_URL, install_location)
            except GitCommandError as e:
                print(f"{Fore.RED}Directory not empty.{Fore.RESET}\nInstall manually, or choose another location.")
                return None
        
    install_location = os.path.normpath(input("Install into: "))
    try:
        return Repo.clone_from(REPO_URL, install_location)
    except GitCommandError as e:
        print(f"{Fore.RED}Directory not empty.{Fore.RESET}\nInstall manually, or choose another location.\n")
        return None

def main():
    colorama.init(autoreset=True)
    repo = clone()
    if not repo:
        return
    print(f"Cloned into: {repo.working_dir}")


if __name__ == '__main__':
    main()