# HexaSafeLink

**HexaSafeLink CLI** is a lightweight Python tool to detect scam & suspicious links worldwide.

## Features
- Shortlink detection (bit.ly, tinyurl, t.co etc.)
- Suspicious TLD & keyword detection (.xyz, .top, free, gift, win, etc.)
- DNS/IP check & risk scoring
- Colorful CLI output with summary

## Installation (venv or system Python)
```bash
# optional: create venv
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# install HexaSafeLink CLI
pip install -e .

# test CLI
hexasafelink https://bit.ly/freebitcoin

##Usage
hexasafelink <url>
