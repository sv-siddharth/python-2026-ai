# day35_authentication_api_keys_headers.py

"""
Day 35 - Authentication APIs
API Keys, Headers, dotenv, Environment Variables

Topics Covered:
1. API authentication
2. Headers
3. Bearer tokens
4. Environment variables
5. dotenv usage
6. Secure API requests
"""

# ==============================
# SECTION 1 — IMPORTS
# ==============================

import os
import requests
from dotenv import load_dotenv


# ==============================
# SECTION 2 — LOAD .env FILE
# ==============================

# Loads variables from .env into environment variables
load_dotenv()


# ==============================
# SECTION 3 — READ ENVIRONMENT VARIABLE
# ==============================

# Reads OPENAI_API_KEY from environment
API_KEY = os.getenv("OPENAI_API_KEY")

# Safety check
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")


# ==============================
# SECTION 4 — CREATE HEADERS
# ==============================

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


# ==============================
# SECTION 5 — SIMPLE AUTH TEST
# ==============================

print("\n===== AUTHENTICATION TEST =====\n")

response = requests.get(
    "https://httpbin.org/bearer",
    headers=headers
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)


# ==============================
# SECTION 6 — VIEW HEADERS SENT
# ==============================

print("\n===== HEADERS TEST =====\n")

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())


# ==============================
# SECTION 7 — GET REQUEST EXAMPLE
# ==============================

print("\n===== GET REQUEST EXAMPLE =====\n")

params = {
    "name": "Siddharth",
    "course": "Python"
}

response = requests.get(
    "https://httpbin.org/get",
    params=params,
    headers=headers
)

print("Final URL:")
print(response.url)

print("\nJSON Response:")
print(response.json())


# ==============================
# SECTION 8 — POST REQUEST EXAMPLE
# ==============================

print("\n===== POST REQUEST EXAMPLE =====\n")

data = {
    "message": "Hello API",
    "topic": "Authentication"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data,
    headers=headers
)

print("Status Code:", response.status_code)

print("\nReturned JSON:")
print(response.json())


# ==============================
# SECTION 9 — HANDLE AUTH ERRORS
# ==============================

print("\n===== ERROR HANDLING =====\n")

fake_headers = {
    "Authorization": "Bearer wrong_key"
}

response = requests.get(
    "https://httpbin.org/status/401",
    headers=fake_headers
)

if response.status_code == 401:
    print("Authentication failed!")
else:
    print("Request successful")


# ==============================
# SECTION 10 — FUNCTION FOR AUTH REQUESTS
# ==============================

def make_authenticated_get_request(url, headers):
    """
    Makes authenticated GET request
    """

    try:
        response = requests.get(url, headers=headers)

        print("\nRequest Successful")
        print("Status Code:", response.status_code)

        return response

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


print("\n===== FUNCTION EXAMPLE =====\n")

make_authenticated_get_request(
    "https://httpbin.org/get",
    headers
)


# ==============================
# SECTION 11 — CLASS-BASED API CLIENT
# ==============================

class APIClient:

    def __init__(self, api_key):
        self.api_key = api_key

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_data(self, url):

        response = requests.get(
            url,
            headers=self.headers
        )

        return response.json()

    def post_data(self, url, data):

        response = requests.post(
            url,
            json=data,
            headers=self.headers
        )

        return response.json()


print("\n===== CLASS-BASED CLIENT =====\n")

client = APIClient(API_KEY)

response = client.get_data("https://httpbin.org/get")

print(response)


# ==============================
# SECTION 12 — IMPORTANT NOTES
# ==============================

"""
IMPORTANT FILES

1. .env

OPENAI_API_KEY=your_secret_key_here


2. .gitignore

.env


IMPORTANT COMMANDS

pip install requests
pip install python-dotenv


KEY CONCEPTS

1. load_dotenv()
   Loads .env file into environment variables

2. os.getenv("KEY")
   Reads variable from environment

3. Headers
   Send metadata with requests

4. Authorization
   Used for authentication

5. Bearer Token
   Standard API authentication format

6. NEVER hardcode API keys
"""


print("\n===== DAY 35 COMPLETE =====")