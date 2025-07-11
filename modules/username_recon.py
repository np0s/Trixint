import requests
import webbrowser

SITES = {
    'GitHub': 'https://github.com/{}',
    'Twitter': 'https://twitter.com/{}',
    'Instagram': 'https://www.instagram.com/{}/',
    'Reddit': 'https://www.reddit.com/user/{}/',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'TikTok': 'https://www.tiktok.com/@{}',
}

def check_username(username: str) -> dict:
    """
    Checks if the username exists on various social media platforms.
    Returns a dictionary {site: True/False}.
    """
    results = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    for site, url_template in SITES.items():
        url = url_template.format(username)
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            if site == 'TikTok':
                # TikTok returns 200 for not found, but with a special page
                results[site] = 'tiktok' not in resp.url.lower() and resp.status_code == 200
            else:
                results[site] = resp.status_code == 200
        except Exception:
            results[site] = False
    return results

def print_results(results, username):
    print(f"\nUsername check results for: {username}\n" + "-"*40)
    for site, exists in results.items():
        status = "Exists" if exists else "Not found"
        print(f"{site:10}: {status}")
    print("-"*40)

def open_profiles(results, username):
    for site, found in results.items():
        if found:
            url = SITES[site].format(username)
            webbrowser.open(url) 