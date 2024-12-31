#import libraries
import os
import lob
from dotenv import load_dotenv

#import get_address and postcard templates
from get_address import get_address
from templates import html_front_template_1, html_front_template_2, html_back_template_1, html_back_template_2

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

  if version == 1: 
    back_html = html_back_template_1.replace('{{name}}', recipient_name)
    front_html = html_front_template_1
  elif version == 2:
    back_html = html_back_template_2.replace('{{name}}', recipient_name)
    front_html = html_front_template_2

  # Create a postcard using the corrected parameters
  postcard = lob.Postcard.create(
      description="Personalized Postcard",
      to_address=address_id_to_send_to,
      from_address=from_address_lob_id,  #Lob's address in SF
      front=front_html,
      back=back_html,
      size="4x6",  #"4x6", "6x9"
      use_type="marketing"
  )

  return postcard

print(create_postcard('adr_2ad9772142b75ffe', 2))