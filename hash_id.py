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

