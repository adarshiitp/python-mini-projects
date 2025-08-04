import random
import string
import pyperclip

def check_strength(pwd):
    if len(pwd) < 6:
        return "❌ Weak"
    elif len(pwd) < 10:
        if any(c in string.punctuation for c in pwd):
            return "🟡 Medium"
        else:
            return "⚠️ Medium"
    else:
        if (any(c in string.digits for c in pwd) and
            any(c in string.punctuation for c in pwd) and
            any(c.isupper() for c in pwd)):
            return "✅ Strong"
        else:
            return "🟡 Medium"

length = int(input("Enter Your password length = "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(chars, length))

print("🔐 Your Generated Password is:", password)
print("🔎 Strength:", check_strength(password))

a  = input("Copy to clipboard (yes/no)=").lower()

if a == 'yes':
    pyperclip.copy(password)
    print("📋 Password copied to clipboard!")



