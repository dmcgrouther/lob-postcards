#import libraries
import os
import lob
from dotenv import load_dotenv
import json

#import get_address and postcard templates
from get_address import get_address
from templates import html_front_template_1, html_front_template_2, html_back_template, qr_code_a, qr_code_b

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")
lob.api_key = LOB_API_KEY  # Initialize the Lob API key

# from address - Lob HQ
from_address_lob_id = 'adr_10bef0fa55e04b71'
from_address_lob = get_address(from_address_lob_id, LOB_API_KEY)
from_name = from_address_lob.get('name', 'Default Name')  # Extract the name from the "from address"

def create_postcard(address_id_to_send_to, version):
    recipient_address = get_address(address_id_to_send_to, LOB_API_KEY)
    recipient_address['address_country'] = 'US'  # Add the correct ISO-3166 country code
    recipient_name = recipient_address.get("name", "Neighbor")  # Extract recipient name or set default

    # Replace placeholders in back HTML template
    back_html = html_back_template.replace('{{name}}', recipient_name)

    # Handle A/B testing for QR codes
    if version == 1: 
        front_html = html_front_template_1
        back_html = back_html.replace("{{qr_code_url}}", qr_code_a)
    elif version == 2:
        front_html = html_front_template_2
        back_html = back_html.replace("{{qr_code_url}}", qr_code_b)

    # Create a postcard using the corrected parameters
    postcard = lob.Postcard.create(
        description="Personalized Postcard",
        to_address=address_id_to_send_to,
        from_address=from_address_lob_id,  # Lob's address in SF
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
    count=0
    for address in address_list:
        if count % 2 == 0:
            print(create_postcard(address['id'], 1))
        if count % 2 != 0:
            print(create_postcard(address['id'], 2))
        count=count+1

create_postcards(addresses)