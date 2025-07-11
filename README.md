# Trixint

Trixint is a CLI Python OSINT (Open Source Intelligence) tool for username reconnaissance across popular social media platforms. It helps you quickly check if a username exists on GitHub, Twitter, Instagram, Reddit, Pinterest, and TikTok.

## Features

- Check username existence on multiple platforms with a single command
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

Run the tool from the command line:

```bash
python main.py
```

You will be prompted to enter a username. The tool will then check the username across supported platforms and display the results.

## Project Structure

- `main.py`: Entry point for the CLI tool
- `modules/username_recon.py`: Username reconnaissance logic
- `requirements.txt`: Python dependencies

## Future Plans

- Add support for more social media and web platforms
- Export results to CSV/JSON
- Add batch username checking
- Improve error handling and detection logic
- Add advanced OSINT modules (email, phone, etc.)
- Docker support for easy deployment

---

Contributions and suggestions are welcome! 