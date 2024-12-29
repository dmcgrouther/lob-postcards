#import libraries
import requests
import os
import lob
from dotenv import load_dotenv

#import get_address
from get_address import get_address

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")
lob.api_key = LOB_API_KEY  # Initialize the Lob API key

# Sample address
test_address = 'adr_10bef0fa55e04b71'

#retrieve sample address
from_address = get_address(test_address, LOB_API_KEY)
recepient_name = from_address.get("name")

# Example recipient address
to_address = {
    'name': recepient_name,
    'address_line1': "1600 Amphitheatre Parkway",
    'address_city': "Mountain View",
    'address_state': 'CA',
    'address_zip': '94043',
    'address_country': 'US'
}

# Create the "to address" in Lob
to_address_obj = lob.Address.create(
    name=to_address['name'],
    address_line1=to_address['address_line1'],
    address_city=to_address['address_city'],
    address_state=to_address['address_state'],
    address_zip=to_address['address_zip'],
    address_country=to_address['address_country']
)

# Extract the name from the "from address"
from_name = from_address.get('name', 'Default Name')

# Example HTML template for the front of the postcard with a placeholder for the name
html_front_template = """
<html>
  <body>
    <h1>Hello {{name}}!</h1>
    <p>This is a personalized postcard sent using Lob.</p>
  </body>
</html>
"""

# Example HTML template for the back of the postcard
html_back_template = """
<html>
  <body>
    <p>This is the back of the postcard.</p>
    <p>Addressed to {{name}}</p>
  </body>
</html>
"""

# Replace placeholders with dynamic content
front_html = html_front_template.replace('{{name}}', from_name)
back_html = html_back_template.replace('{{name}}', recepient_name)

# Create a postcard using the corrected parameters
postcard = lob.Postcard.create(
    description="Personalized Postcard",
    to_address=to_address_obj['id'],
    from_address=test_address,  # Use the existing address ID
    front=front_html,
    back=back_html,
    size="4x6",  # You can choose the size of the postcard, such as "4x6" or "5x7"
    use_type="marketing"
)

print(f"Postcard created! View it here: {postcard['url']}")