import os
from dotenv import load_dotenv

# 🔍 Explicit path to .env (prints for debugging)
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".env")
print("Looking for .env at:", dotenv_path)

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print("✅ .env loaded.")
else:
    print("❌ .env file NOT found.")

# ✅ Print values to confirm they're loaded
print("TestRail URL:", os.getenv("TESTRAIL_URL"))
print("TestRail User:", os.getenv("TESTRAIL_USER"))
print("API Key Length:", len(os.getenv("TESTRAIL_API_KEY") or ""))

from testrail_api import TestRailAPI

# 🔐 Initialize TestRail API
api = TestRailAPI(
    os.getenv("TESTRAIL_URL"),
    os.getenv("TESTRAIL_USER"),
    os.getenv("TESTRAIL_API_KEY")
)

def create_test_case(project_id, suite_id, section_id, title, steps):
    return api.cases.add_case(section_id, {
        "title": title,
        "custom_steps_separated": steps,
        "type_id": 1,
        "priority_id": 2
    })
