# main.py

import argparse
from modules.username_recon import check_username, print_results, open_profiles
from modules.phone_recon import parse_phone_number, print_phone_info

parser = argparse.ArgumentParser()
parser.add_argument("username", nargs="?", help="Username to check")
parser.add_argument("--open", action="store_true", help="Open found profiles in browser")
parser.add_argument("--phone", help="Phone number to analyze (with country code, e.g. +12025550123)")
args = parser.parse_args()

if args.phone:
    info = parse_phone_number(args.phone)
    print_phone_info(info, args.phone)

if args.username:
    results = check_username(args.username)
    print_results(results, args.username)
    if args.open:
        open_profiles(results, args.username) 