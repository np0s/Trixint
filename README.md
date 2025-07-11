# Trixint

Trixint is a CLI Python OSINT (Open Source Intelligence) tool for username and phone number reconnaissance across popular social media platforms and telecom numbering plans. It helps you quickly check if a username exists on dozens of sites, and analyze phone numbers for validity, region, and carrier info.

## Features

- Check username existence on 30+ social and web platforms with a single command
- Phone number OSINT: parse, validate, get country, region, carrier, and type
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

### Username Reconnaissance
Check if a username exists across many platforms:
```bash
python main.py <username>
```
Add `--open` to open found profiles in your browser:
```bash
python main.py <username> --open
```

### Phone Number OSINT
Analyze a phone number for validity, country, region, carrier, and type:
```bash
python main.py --phone <number>
```
- **Tip:** For best results, use international format (e.g. `+12025550123`).
- If you enter a number without a country code, the tool will guess the region (e.g. 10 digits starting with 7/8/9 = India, otherwise US). This is not always accurate.

#### Example:
```bash
python main.py --phone +918113900396
```

### Combined Usage
You can check both a username and a phone number in one command:
```bash
python main.py <username> --phone <number>
```

## Limitations
- **Phone number checks:**
  - The tool CANNOT tell you who owns a number, if it is currently assigned, or when it was last used.
  - It only checks if the number is possible/valid for a region and provides carrier/type info if available.
  - Always use international format for best accuracy.
- **Username checks:**
  - Some platforms may block automated requests or change their profile URL patterns.

## Project Structure

- `main.py`: Entry point for the CLI tool
- `modules/username_recon.py`: Username reconnaissance logic
- `modules/phone_recon.py`: Phone number OSINT logic
- `requirements.txt`: Python dependencies

## Future Plans

- Add support for more social media and web platforms
- Export results to CSV/JSON
- Add batch username and phone checking
- Improve error handling and detection logic
- Add advanced OSINT modules (email, data breach, etc.)
- Docker support for easy deployment

---

Contributions and suggestions are welcome!
