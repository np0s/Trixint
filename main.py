# main.py

import argparse
from modules.username_recon import check_username, print_results, open_profiles

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username to check")
parser.add_argument("--open", action="store_true", help="Open found profiles in browser")
args = parser.parse_args()

results = check_username(args.username)
print_results(results, args.username)
if args.open:
    open_profiles(results, args.username) 