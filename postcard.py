import os
import lob
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set the Lob API key
LOB_API_KEY = os.getenv("LOB_API_KEY")
lob.api_key = LOB_API_KEY  # Initialize the Lob API key

# Example sender (from address)
from_address = lob.Address.create(
    name="John Doe",
    address_line1="123 Main Street",
    address_city="San Francisco",
    address_state="CA",
    address_zip="94158",
    address_country="US",
)

# Example recipient (to address)
to_address = lob.Address.create(
    name="Jane Smith",
    address_line1="1600 Amphitheatre Parkway",
    address_city="Mountain View",
    address_state="CA",
    address_zip="94043",
    address_country="US",
)

# HTML templates for the postcard
front_template = """
<html>
  <body>
    <h1>Hello {{name}}!</h1>
    <p>This is the front of your postcard.</p>
  </body>
</html>
"""

back_template = """
<html>
  <body>
    <h1>Thank You, {{name}}!</h1>
    <p>This is the back of your postcard, where your message goes.</p>
  </body>
</html>
"""

# Replace placeholders in the templates
customized_front = front_template.replace("{{name}}", to_address["name"])
customized_back = back_template.replace("{{name}}", to_address["name"])

# Create the postcard
try:
    postcard = lob.Postcard.create(
        description="Personalized Postcard Example",
        to_address=to_address["id"],  # Use the ID of the created to_address
        from_address=from_address["id"],  # Use the ID of the created from_address
        front=customized_front,  # Content for the front of the postcard
        back=customized_back,  # Content for the back of the postcard
        size="4x6",  # Choose postcard size, e.g., "4x6" or "5x7"
        use_type="marketing"
    )

    # Print the postcard URL
    print(f"Postcard created! View it here: {postcard['url']}")

except lob.error.LobError as e:
    print(f"An error occurred: {e}")
