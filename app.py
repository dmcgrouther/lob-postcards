#import libraries
import os
import lob
from dotenv import load_dotenv

#import get_address and postcard templates
from get_address import get_address
from templates import html_front_template_1, html_front_template_2, html_front_template_3, html_back_template

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")
lob.api_key = LOB_API_KEY  # Initialize the Lob API key

# from address - Lob HQ
from_address_lob_id = 'adr_10bef0fa55e04b71'
from_address_lob = get_address(from_address_lob_id, LOB_API_KEY)
from_name = from_address_lob.get('name', 'Default Name')  # Extract the name from the "from address"

#send to sample address
sample_address_id = 'adr_2ad9772142b75ffe'
recipient_address = get_address(sample_address_id, LOB_API_KEY)
recipient_address['address_country'] = 'US'  # Add the correct ISO-3166 country code
recipient_name = recipient_address.get("name", "Neighbor")  # Extract recipient name or set default

# Replace placeholders with dynamic content
back_html = html_back_template.replace('{{name}}', recipient_name)

# Create a postcard using the corrected parameters
postcard = lob.Postcard.create(
    description="Personalized Postcard",
    to_address=sample_address_id,
    from_address=from_address_lob_id,  #Lob's address in SF
    front=html_front_template_2, #another template html_front_template_1
    back=back_html,
    size="4x6",  # You can choose the size of the postcard, such as "4x6" or "5x7"
    use_type="marketing"
)

print(f"Postcard created! View it here: {postcard['url']}")