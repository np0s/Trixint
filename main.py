# main.py

import argparse
from modules.username_recon import check_username, print_results, open_profiles
from modules.phone_recon import parse_phone_number, print_phone_info
from modules.gui import run_gui

def main():
    parser = argparse.ArgumentParser(description="Trixint - OSINT Tool for username and phone reconnaissance")
    parser.add_argument("username", nargs="?", help="Username to check")
    parser.add_argument("--open", action="store_true", help="Open found profiles in browser")
    parser.add_argument("--phone", help="Phone number to analyze (with country code, e.g. +12025550123)")
    parser.add_argument("--cli", action="store_true", help="Force CLI mode (default)")
    parser.add_argument("--gui", action="store_true", help="Launch graphical interface")
    
    args = parser.parse_args()
    
    # GUI mode
    if args.gui:
        run_gui()
        return
    
    # CLI mode (default)
    if args.phone:
        info = parse_phone_number(args.phone)
        print_phone_info(info, args.phone)
    
    if args.username:
        results = check_username(args.username)
        print_results(results, args.username)
        if args.open:
            open_profiles(results, args.username)
    
    # If no username or phone provided, show help
    if not args.username and not args.phone and not args.gui:
        parser.print_help()

if __name__ == "__main__":
    main() 