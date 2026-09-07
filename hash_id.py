import re

def identify_hash(h):
    h = h.strip()
    
    if h.startswith("$argon2"):
        return "Argon2"
    if h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$"):
        return "bcrypt"
    if re.fullmatch(r"[a-fA-F0-9]{32}", h):
        return "MD5"
    if re.fullmatch(r"[a-fA-F0-9]{40}", h):
        return "SHA-1"
    if re.fullmatch(r"[a-fA-F0-9]{64}", h):
        return "SHA-256"
    
    return "Unknown"

if __name__ == "__main__":
    test = input("Enter a hash: ")
    print("Type:", identify_hash(test))

# Hash Identifier 🔍

A simple Python tool that identifies the type of a cryptographic hash (MD5, SHA-1, SHA-256, bcrypt, Argon2) based on its length, prefix, and character set.

This was my first cybersecurity project, built to practice pattern recognition around hashing algorithms — a skill used in password cracking, digital forensics, and general security auditing.

## Features

- Detects common hash types: MD5, SHA-1, SHA-256, bcrypt, Argon2
- Works via simple, fast pattern matching (no external libraries needed)
- Easy to extend with more hash types

## How to Run

Requires Python 3.

```bash
python3 hash_id.py
```

You'll be prompted to enter a hash, and the tool will print the detected type.

## Example

```
Enter a hash: 5f4dcc3b5aa765d61d8327deb882cf99
Type: MD5
```

## How It Works

Every hash algorithm produces output with a recognizable "fingerprint":

| Hash type | Length    | Pattern                        |
|-----------|-----------|---------------------------------|
| MD5       | 32 chars  | hex only (0-9, a-f)             |
| SHA-1     | 40 chars  | hex only                        |
| SHA-256   | 64 chars  | hex only                        |
| bcrypt    | 60 chars  | starts with `$2a$` / `$2b$` / `$2y$` |
| Argon2    | varies    | starts with `$argon2`           |

The script checks these rules in order and returns the first match.

## What I Learned

- The structural differences between common hashing algorithms
- How to use Python's `re` module for pattern matching
- The basics of building and documenting a small CLI tool

## Next Steps

- Add support for more hash types (e.g. NTLM, SHA-512)
- Handle salted hashes
- Turn it into a proper CLI tool with arguments (e.g. `python3 hash_id.py --hash <value>`)
