"""
Day 15 - Local Development Environment (Python Setup, pip, venv)

This file acts like a README + executable guide.

GOAL:
- Understand pip (Python package manager)
- Use virtual environments (venv)
- Work with environment variables (.env)
- Build a small real-world CLI tool

IMPORTANT:
This is one of the MOST important days for becoming a real developer.
Everything in AI (LangChain, FastAPI, OpenAI) depends on this setup.
"""

# ==========================================================
# 🧠 SECTION 1: WHAT IS PIP?
# ==========================================================

"""
pip = Python package manager (like npm in JavaScript)

Used to install external libraries.

Examples (run in terminal, NOT in Python file):

    pip install requests
    pip uninstall requests
    pip list
    pip freeze > requirements.txt
    pip install -r requirements.txt
"""

# ==========================================================
# 🧪 SECTION 2: VIRTUAL ENVIRONMENTS (CRITICAL)
# ==========================================================

"""
WHY venv?

Without venv:
- All packages install globally
- Projects conflict with each other
- Version issues break apps

With venv:
- Each project is isolated
- Clean dependency management

Commands (run in terminal):

1. Create virtual environment:
    python -m venv venv

2. Activate (Mac/Linux):
    source venv/bin/activate

3. Activate (Windows):
    venv\\Scripts\\activate

4. Deactivate:
    deactivate
"""

# ==========================================================
# 🔐 SECTION 3: ENVIRONMENT VARIABLES (.env)
# ==========================================================

"""
WHY use .env?

Never hardcode secrets like API keys.

BAD:
    API_KEY = "123abc"

GOOD:
    Store in .env file:
        API_KEY=123abc

Install dotenv:
    pip install python-dotenv
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

print("Loaded API Key:", api_key)  # Will print None if not set


# ==========================================================
# 🌐 SECTION 4: USING EXTERNAL LIBRARIES (requests)
# ==========================================================

"""
We use 'requests' library to call APIs.

Install:
    pip install requests
"""

import requests


def get_weather(city):
    """
    Calls a free weather API and returns result.
    """
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            return response.text
        else:
            return "Error fetching weather"

    except Exception as e:
        return f"Exception occurred: {e}"


# ==========================================================
# 🧪 SECTION 5: CLI TOOL (REAL PROJECT)
# ==========================================================

"""
We now combine everything into a CLI tool.

This satisfies your Phase 1 milestone:
✔ External API call
✔ Uses installed package
✔ Structured function
"""


def main():
    print("\n🌦️ Simple Weather CLI Tool\n")

    city = input("Enter city name: ")

    result = get_weather(city)

    print("\nWeather Info:")
    print(result)


# ==========================================================
# 🚀 ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()


# ==========================================================
# 📁 SECTION 6: PROJECT STRUCTURE (IMPORTANT)
# ==========================================================

"""
Your project should look like this:

my_project/
│
├── venv/               # Virtual environment (DO NOT PUSH TO GITHUB)
├── day_15_environment_setup.py
├── requirements.txt    # pip freeze output
└── .env               # environment variables

IMPORTANT:
- Add venv/ and .env to .gitignore
"""


# ==========================================================
# 🧠 SECTION 7: JS → PYTHON MAPPING
# ==========================================================

"""
JavaScript           → Python
--------------------------------
npm install         → pip install
package.json        → requirements.txt
node_modules        → venv
process.env         → os.getenv()
npx                 → python -m

This mapping is VERY important for you.
"""


# ==========================================================
# 🎯 FINAL TAKEAWAYS
# ==========================================================

"""
After Day 15, you should be able to:

✔ Create virtual environments
✔ Install packages using pip
✔ Use environment variables securely
✔ Build CLI tools
✔ Structure real projects

THIS is what separates:
Beginner → Developer

Next:
You are now ready for real backend + AI work.
"""