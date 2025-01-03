#import libraries
import os
import lob
from dotenv import load_dotenv
import json

#import get_address and postcard templates
from get_address import get_address
from templates import html_front_templates, html_back_template, qr_codes

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")
lob.api_key = LOB_API_KEY  # Initialize the Lob API key

# from address - Compass
from_address_compass_id = 'adr_c7df05a406f9e9bb'
from_address_compass = get_address(from_address_compass_id, LOB_API_KEY)
from_name = from_address_compass.get('name', 'Compass')  # Extract the name from the "from address"

def create_postcard(address_id_to_send_to, version):
    recipient_address = get_address(address_id_to_send_to, LOB_API_KEY)
    recipient_address['address_country'] = 'US'  # Add the correct ISO-3166 country code
    recipient_name = recipient_address.get("name", "Neighbor")  # Extract recipient name or set default

    # Replace placeholders in back HTML template
    back_html = html_back_template.replace('{{name}}', recipient_name)
    back_html = back_html.replace("{{qr_code_url}}", qr_codes[version % len(qr_codes)])

    # Select front template
    front_html = html_front_templates[version % len(html_front_templates)]

    # Create the postcard
    postcard = lob.Postcard.create(
        description="Personalized Postcard",
        to_address=address_id_to_send_to,
        from_address=from_address_compass_id,  # Compass's address in SF
        front=front_html,
        back=back_html,
        size="4x6",  # "4x6", "6x9"
        use_type="marketing"
    )

    return postcard

#Create one post card. Version 1 or 2
# print(create_postcard('adr_82cccf57d2b090f0', 1))
# print(create_postcard('adr_82cccf57d2b090f0', 2))

def load_address_ids(filename):
    with open(filename, "r") as file:
        return json.load(file)
    
addresses = load_address_ids("data.json")

def create_postcards(address_list):
    for i, address in enumerate(address_list):
        version = i % len(html_front_templates)  # Cycle through versions dynamically. This ensures randomness for trying different version
        print(create_postcard(address['id'], version))

create_postcards(addresses)