# Day 34 - API Project (Real-World Usage)
# Complete Notes + Examples + Mini Project

import requests
import json

# =========================================================
# 1. BASIC GET REQUEST
# =========================================================

print("===== BASIC GET REQUEST =====")

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Response Type:", type(response))
print()


# =========================================================
# 2. CONVERT RESPONSE TO JSON
# =========================================================

print("===== JSON RESPONSE =====")

data = response.json()

print("Data Type:", type(data))
print("Current User URL:", data["current_user_url"])
print()


# =========================================================
# 3. QUERY PARAMETERS
# =========================================================

print("===== QUERY PARAMETERS =====")

params = {
    "q": "python"
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

print("Final URL:", response.url)
print("Status Code:", response.status_code)
print()


# =========================================================
# 4. HEADERS
# =========================================================

print("===== HEADERS =====")

headers = {
    "User-Agent": "PythonLearningApp"
}

response = requests.get(
    "https://api.github.com",
    headers=headers
)

print("Status Code:", response.status_code)
print()


# =========================================================
# 5. POST REQUEST
# =========================================================

print("===== POST REQUEST =====")

payload = {
    "name": "Siddharth",
    "role": "AI Engineer"
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload
)

print("POST Status:", response.status_code)

post_data = response.json()

print("Returned JSON:")
print(json.dumps(post_data, indent=4))
print()


# =========================================================
# 6. ERROR HANDLING
# =========================================================

print("===== ERROR HANDLING =====")

try:
    response = requests.get(
        "https://api.github.com",
        timeout=5
    )

    response.raise_for_status()

    print("Request successful!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.Timeout:
    print("Request Timed Out")

except requests.exceptions.RequestException as e:
    print("General Request Error:", e)

print()


# =========================================================
# 7. SAVE JSON TO FILE
# =========================================================

print("===== SAVE JSON TO FILE =====")

response = requests.get("https://api.github.com")

data = response.json()

with open("github_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved to github_data.json")
print()


# =========================================================
# 8. LOAD JSON FROM FILE
# =========================================================

print("===== LOAD JSON FROM FILE =====")

with open("github_data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded Current User URL:")
print(loaded_data["current_user_url"])
print()


# =========================================================
# 9. MINI PROJECT - WEATHER APP
# =========================================================

print("===== WEATHER APP =====")

API_KEY = "your_api_key_here"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(
        BASE_URL,
        params=params,
        timeout=5
    )

    response.raise_for_status()

    weather_data = response.json()

    city_name = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")

except requests.exceptions.HTTPError:
    print("Invalid city name or API issue.")

except requests.exceptions.ConnectionError:
    print("Internet connection problem.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except Exception as e:
    print("Unexpected error:", e)

print()


# =========================================================
# 10. AI API STRUCTURE EXAMPLE
# =========================================================

print("===== AI API STRUCTURE EXAMPLE =====")

API_KEY = "your_openai_api_key"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

json_data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "Hello AI"
        }
    ]
}

print("Example OpenAI-style request prepared.")
print()


# =========================================================
# 11. IMPORTANT NOTES
# =========================================================

"""
KEY CONCEPTS LEARNED TODAY:

1. requests.get()
2. requests.post()
3. response.json()
4. Query parameters
5. Headers
6. API keys
7. JSON handling
8. Error handling
9. Saving API data
10. Real-world API project

VERY IMPORTANT FOR:
- OpenAI APIs
- Anthropic APIs
- LangChain
- RAG pipelines
- AI agents
- FastAPI
"""