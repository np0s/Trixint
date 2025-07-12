import requests
import webbrowser

SITES = {
    'GitHub': 'https://github.com/{}',
    'Twitter': 'https://twitter.com/{}',
    'Instagram': 'https://www.instagram.com/{}/',
    'Reddit': 'https://www.reddit.com/user/{}/',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'TikTok': 'https://www.tiktok.com/@{}',
    'Facebook': 'https://www.facebook.com/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'YouTube': 'https://www.youtube.com/{}',
    'SoundCloud': 'https://soundcloud.com/{}',
    'VK': 'https://vk.com/{}',
    'Mastodon.social': 'https://mastodon.social/@{}',
    'Medium': 'https://medium.com/@{}',
    'DeviantArt': 'https://www.deviantart.com/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'Discord': 'https://discord.com/users/{}',
    'Quora': 'https://www.quora.com/profile/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'Steam': 'https://steamcommunity.com/id/{}',
    'GitLab': 'https://gitlab.com/{}',
    'Bitbucket': 'https://bitbucket.org/{}',
    'Replit': 'https://replit.com/@{}',
    'Keybase': 'https://keybase.io/{}',
    'Patreon': 'https://www.patreon.com/{}',
    'Behance': 'https://www.behance.net/{}',
    '500px': 'https://500px.com/{}',
    'About.me': 'https://about.me/{}',
    'AngelList': 'https://angel.co/u/{}',
    'ProductHunt': 'https://www.producthunt.com/@{}',
    'Goodreads': 'https://www.goodreads.com/{}',
    'TripAdvisor': 'https://www.tripadvisor.com/members/{}',
    'Badoo': 'https://badoo.com/profile/{}',
    'OKCupid': 'https://www.okcupid.com/profile/{}',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'Vimeo': 'https://vimeo.com/{}',
    'Mixcloud': 'https://www.mixcloud.com/{}',
    'Bandcamp': 'https://bandcamp.com/{}',
    'Dribbble': 'https://dribbble.com/{}',
    'Kaggle': 'https://www.kaggle.com/{}',
    'Last.fm': 'https://www.last.fm/user/{}',
    'Roblox': 'https://www.roblox.com/user.aspx?username={}',
    'Wattpad': 'https://www.wattpad.com/user/{}',
    'WordPress': 'https://{}.wordpress.com',
    'Tumblr': 'https://{}.tumblr.com',
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
        print(f"{site:15}: {status}")
    print("-"*40)

def open_profiles(results, username):
    for site, found in results.items():
        if found is True:
            url = SITES[site].format(username)
            webbrowser.open(url) 