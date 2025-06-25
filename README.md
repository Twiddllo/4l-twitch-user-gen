> **Note:** This code was created for an earlier time. As of now, Twitch protections have blocked this method for checking usernames, and it may no longer work as intended.

# Twitch Username Availability Checker

This Python script checks the availability of Twitch usernames using the Twitch GraphQL API. It can check usernames from a list or generate random usernames, and supports both single-run and continuous checking modes. Colored output is provided for easy result distinction.

## Features
- Checks Twitch username availability via the official API
- Supports checking from a list (`user.txt`) or generating random usernames
- Configurable username length and number of checks
- Colored terminal output (green for available, red for taken)
- Multi-threaded for faster checking

## Requirements
- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [colorama](https://pypi.org/project/colorama/)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

1. **Configure the script:**
   - Edit `config.json` to set your preferences (see below).
   - Optionally, add usernames to `user.txt` (one per line) to check specific names.

2. **Run the script:**
```bash
python main.py
```

## Configuration (`config.json`)

| Key        | Type    | Description                                                                 |
|------------|---------|-----------------------------------------------------------------------------|
| numbers    | bool    | (Unused in current script)                                                  |
| while      | bool    | `true` for continuous checking (infinite loop), `false` for fixed amount     |
| ammount    | int     | Number of usernames to check (if `while` is `false`)                        |
| letters    | int     | Number of letters for randomly generated usernames                          |

Example:
```json
{
    "numbers": false,
    "while": false,
    "ammount": 100,
    "letters": 5
}
```

## Username Sources
- If `user.txt` contains usernames (one per line), the script will check those first.
- If `user.txt` is empty or all names are used, it will generate random usernames of length `letters`.

## Output
- **Green `+`**: Username is available
- **Red `-`**: Username is taken

## Notes
- The `numbers` config option is present but not used in the current script.
- The script uses multi-threading for speed, but Twitch may rate-limit excessive requests.
- `colorama` is used for colored output. On Windows, it should work out of the box, but if you have issues, see the [Colorama docs](https://pypi.org/project/colorama/).

## Files
- `main.py` — Main script
- `config.json` — Configuration file
- `user.txt` — List of usernames to check (optional, one per line)
- `requirements.txt` — Python dependencies

## License
This project is provided as-is for educational and personal use.

**Note:** This code was created for an earlier time. As of now, Twitch protections have blocked this method for checking usernames, and it may no longer work as intended.
