import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    try:
        response_json = response.json()
    except (ValueError, requests.exceptions.JSONDecodeError):
        print(f"Error: Invalid JSON response from API")
        return {}

    data = response_json.get("person")

    if data is None:
        print(f"Error: No 'person' data found in API response")
        print(f"Response content: {response_json}")
        return {}

    if not isinstance(data, dict):
        print(f"Error: 'person' data is not a dictionary: {type(data)}")
        return {}

    filtered_data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return filtered_data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
        ),
    )
