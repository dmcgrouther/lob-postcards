import requests
import os
import lob
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")

# Function to fetch an address
def get_address(address_id, api_key):
    url = f"https://api.lob.com/v1/addresses/{address_id}"
    response = requests.get(url, auth=(api_key, ''))
    response.raise_for_status()  # Raise an error if the request fails
    return response.json()

# Test: use the function
# test_address = 'adr_10bef0fa55e04b71'
# address = get_address(test_address, LOB_API_KEY)
# name = address.get("name")