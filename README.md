# Trixint

Trixint is a CLI/GUI Python OSINT (Open Source Intelligence) tool for username and phone number reconnaissance across popular social media platforms and telecom numbering plans. It helps you quickly check if a username exists on dozens of sites, and analyze phone numbers for validity, region, and carrier info.

## Features

- Check username existence on 30+ social and web platforms with a single command
- Phone number OSINT: parse, validate, get country, region, carrier, and type
- **NEW**: Graphical user interface (GUI) for easy point-and-click operation
- Clean, readable CLI output
- Modular codebase for easy extension
- Fast and simple to use

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Trixint
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface (CLI)

**Username OSINT:**
```bash
# Check username
python main.py username

# Check username and open found profiles in browser
python main.py username --open

# Check phone number
python main.py --phone +12025550123

# Check both username and phone
python main.py username --phone +12025550123 --open
```

**Force CLI mode:**
```bash
python main.py --cli username
```

### Graphical User Interface (GUI)

**Launch GUI:**
```bash
python main.py --gui
```

The GUI provides:
- Username input field with "Check Username" button
- Phone number input field with "Check Phone" button
- "Open Found Profiles" button to launch valid profiles in browser
- Real-time results display with status updates
- Threaded operations to keep GUI responsive

### Phone Number Format

For best results, use international format:
- ✅ `+12025550123` (US)
- ✅ `+919876543210` (India)
- ✅ `+447911123456` (UK)

The tool will auto-detect region for common formats, but international format is recommended.

## What Trixint Can Do

### Username OSINT
- Check existence on 30+ platforms including GitHub, Twitter, Instagram, Reddit, Pinterest, TikTok, Facebook, LinkedIn, YouTube, SoundCloud, VK, Mastodon, Medium, DeviantArt, Twitch, Discord, Quora, Flickr, Steam, GitLab, Bitbucket, Replit, Keybase, Patreon, Behance, 500px, About.me, AngelList, ProductHunt, Goodreads, TripAdvisor, Badoo, OKCupid, Snapchat, Vimeo, Mixcloud, Bandcamp, Dribbble, Kaggle, Last.fm, Roblox, Wattpad, WordPress, and Tumblr
- Open found profiles directly in browser
- Clean, organized results display

### Phone Number OSINT
- Parse and validate international phone numbers
- Get country, region, and carrier information
- Detect number type (mobile, landline, etc.)
- Auto-detect region for ambiguous numbers

## What Trixint Cannot Do

### Phone Numbers
- **Cannot identify the owner** (name, address, personal info)
- **Cannot check when last used** or activity status
- **Cannot verify if currently active** or assigned

These limitations are due to privacy laws and require access to private telecom databases.

## Project Structure

```
Trixint/
├── main.py                 # Main entry point
├── modules/
│   ├── username_recon.py   # Username OSINT functions
│   ├── phone_recon.py      # Phone number OSINT functions
│   └── gui.py             # Graphical interface
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Future Plans

- [ ] Add more social media platforms
- [ ] Email OSINT capabilities
- [ ] Domain name reconnaissance
- [ ] Advanced phone number lookups (with paid APIs)
- [ ] Export results to various formats (JSON, CSV, PDF)
- [ ] Batch processing for multiple usernames/numbers
- [ ] Custom platform configuration
- [ ] Rate limiting and proxy support
- [ ] Dark web username checking
- [ ] Integration with other OSINT tools

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve Trixint!

## License

[Add your license here]
