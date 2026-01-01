import requests

# ✅ Directly paste your Relay webhook URL here
RELAY_WEBHOOK_URL = "https://hook.relay.app/api/v1/playbook/cmjvjp7zu2ik70pkofcrz20ml/trigger/tOsxZdeB4QZy3RrmyflYkw"


def get_ai_response(message: str):
    payload = {
        "message": message
    }

    try:
        response = requests.post(
            RELAY_WEBHOOK_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {
            "career_options": ["Error"],
            "required_skills": [],
            "learning_path": "",
            "career_advice": f"Relay error: {str(e)}"
        }
