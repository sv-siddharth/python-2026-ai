"""
DAY 33 — APIs & HTTP Requests with requests Library

Topics Covered:
1. GET requests
2. POST requests
3. JSON handling
4. Query parameters
5. Headers
6. API keys
7. Error handling
8. Timeouts
9. Downloading files
10. Real AI API request example

IMPORTANT:
Install requests first:

pip install requests
"""

import requests
import os
import json
import time


# =========================================================
# 1. SIMPLE GET REQUEST
# =========================================================

print("\n================ SIMPLE GET REQUEST ================\n")

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Response Type:", type(response))

# Raw text response
print("\nRaw Response Text:")
print(response.text[:200])


# =========================================================
# 2. JSON RESPONSE
# =========================================================

print("\n================ JSON RESPONSE ================\n")

data = response.json()

print("JSON Converted To Python Dictionary:")
print(type(data))

print("\nGitHub Current User URL:")
print(data["current_user_url"])


# =========================================================
# 3. PUBLIC API EXAMPLE
# =========================================================

print("\n================ DOG API EXAMPLE ================\n")

dog_response = requests.get(
    "https://dog.ceo/api/breeds/image/random"
)

dog_data = dog_response.json()

print("Random Dog Image URL:")
print(dog_data["message"])


# =========================================================
# 4. QUERY PARAMETERS
# =========================================================

print("\n================ QUERY PARAMETERS ================\n")

params = {
    "q": "python",
    "sort": "stars"
}

github_search = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

print("Generated URL:")
print(github_search.url)

search_data = github_search.json()

print("\nTotal Results:")
print(search_data["total_count"])


# =========================================================
# 5. POST REQUEST
# =========================================================

print("\n================ POST REQUEST ================\n")

payload = {
    "name": "Siddharth",
    "role": "AI Engineer"
}

post_response = requests.post(
    "https://httpbin.org/post",
    json=payload
)

print("POST Status Code:", post_response.status_code)

post_data = post_response.json()

print("\nServer Received:")
print(post_data["json"])


# =========================================================
# 6. HEADERS
# =========================================================

print("\n================ HEADERS ================\n")

headers = {
    "User-Agent": "Python Learning App"
}

header_response = requests.get(
    "https://api.github.com",
    headers=headers
)

print("Status Code:", header_response.status_code)


# =========================================================
# 7. ENVIRONMENT VARIABLES
# =========================================================

print("\n================ ENVIRONMENT VARIABLES ================\n")

# Example:
# export OPENAI_API_KEY="your_key"
# or on Windows:
# setx OPENAI_API_KEY "your_key"

api_key = os.getenv("OPENAI_API_KEY")

print("API Key Exists:", api_key is not None)


# =========================================================
# 8. TIMEOUTS
# =========================================================

print("\n================ TIMEOUT EXAMPLE ================\n")

try:
    timeout_response = requests.get(
        "https://api.github.com",
        timeout=5
    )

    print("Request Successful")

except requests.exceptions.Timeout:
    print("Request Timed Out")


# =========================================================
# 9. ERROR HANDLING
# =========================================================

print("\n================ ERROR HANDLING ================\n")

try:
    bad_response = requests.get(
        "https://api.github.com/invalid-url"
    )

    # Raises exception for bad status codes
    bad_response.raise_for_status()

except requests.exceptions.HTTPError as error:
    print("HTTP Error Occurred:")
    print(error)


# =========================================================
# 10. STATUS CODES
# =========================================================

print("\n================ STATUS CODES ================\n")

print("200 = Success")
print("404 = Not Found")
print("500 = Server Error")
print("401 = Unauthorized")


# =========================================================
# 11. RESPONSE TIME
# =========================================================

print("\n================ RESPONSE TIME ================\n")

response_time = response.elapsed.total_seconds()

print(f"Response Time: {response_time} seconds")


# =========================================================
# 12. SESSIONS
# =========================================================

print("\n================ SESSIONS ================\n")

session = requests.Session()

session.get("https://api.github.com")
session.get("https://api.github.com")

print("Session Reused Successfully")


# =========================================================
# 13. DOWNLOAD FILE
# =========================================================

print("\n================ FILE DOWNLOAD ================\n")

image_url = "https://httpbin.org/image/png"

image_response = requests.get(image_url)

# wb = write binary
with open("sample_image.png", "wb") as file:
    file.write(image_response.content)

print("Image Downloaded Successfully")


# =========================================================
# 14. STREAMING LARGE FILES
# =========================================================

print("\n================ STREAMING EXAMPLE ================\n")

stream_response = requests.get(
    image_url,
    stream=True
)

total_bytes = 0

for chunk in stream_response.iter_content(chunk_size=1024):
    total_bytes += len(chunk)

print("Downloaded Bytes:", total_bytes)


# =========================================================
# 15. CONVERT PYTHON -> JSON
# =========================================================

print("\n================ PYTHON TO JSON ================\n")

person = {
    "name": "Alex",
    "age": 25
}

json_string = json.dumps(person)

print(json_string)
print(type(json_string))


# =========================================================
# 16. CONVERT JSON -> PYTHON
# =========================================================

print("\n================ JSON TO PYTHON ================\n")

text = '{"city": "Delhi", "temperature": 35}'

python_data = json.loads(text)

print(python_data)
print(type(python_data))

print("City:", python_data["city"])


# =========================================================
# 17. WEATHER MINI PROJECT
# =========================================================

print("\n================ WEATHER APP ================\n")

city = input("Enter city name: ")

weather_url = f"https://wttr.in/{city}?format=j1"

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

temperature = weather_data["current_condition"][0]["temp_C"]

print(f"Temperature in {city}: {temperature}°C")


# =========================================================
# 18. GITHUB USER FINDER
# =========================================================

print("\n================ GITHUB USER FINDER ================\n")

username = input("Enter GitHub username: ")

github_url = f"https://api.github.com/users/{username}"

user_response = requests.get(github_url)

if user_response.status_code == 200:

    user_data = user_response.json()

    print("\nUser Information")
    print("----------------")
    print("Name:", user_data["name"])
    print("Followers:", user_data["followers"])
    print("Public Repos:", user_data["public_repos"])

else:
    print("GitHub User Not Found")


# =========================================================
# 19. OPENAI API STYLE REQUEST
# =========================================================

print("\n================ OPENAI API STYLE REQUEST ================\n")

"""
IMPORTANT:

This demonstrates REAL AI engineering structure.

This request may fail if:
1. You do not have an API key
2. Billing is not enabled
3. Internet restrictions exist
"""

if api_key:

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": "Hello AI"
            }
        ]
    }

    try:

        ai_response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=20
        )

        ai_data = ai_response.json()

        print("\nFull AI Response:")
        print(ai_data)

        if "choices" in ai_data:

            reply = ai_data["choices"][0]["message"]["content"]

            print("\nAI Reply:")
            print(reply)

    except Exception as error:
        print("OpenAI Request Failed:")
        print(error)

else:
    print("OPENAI_API_KEY not found")


# =========================================================
# 20. RATE LIMITING
# =========================================================

print("\n================ RATE LIMITING ================\n")

print("Sleeping for 1 second...")
time.sleep(1)
print("Continuing...")


# =========================================================
# 21. COMMON REQUEST EXCEPTIONS
# =========================================================

print("\n================ COMMON EXCEPTIONS ================\n")

print("requests.exceptions.Timeout")
print("requests.exceptions.ConnectionError")
print("requests.exceptions.HTTPError")
print("requests.exceptions.RequestException")


# =========================================================
# 22. FINAL SUMMARY
# =========================================================

print("\n================ DAY 33 SUMMARY ================\n")

print("""
You learned:

1. GET requests
2. POST requests
3. JSON handling
4. Query parameters
5. Headers
6. API authentication
7. Environment variables
8. Error handling
9. File downloading
10. AI API request structure

This is one of the MOST IMPORTANT Python topics
for AI Engineering and backend development.
""")