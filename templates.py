import qrcode
import io
import base64

# # Example HTML templates for the front of the postcards
# html_front_templates = [
#     "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/5eb8636a79f886f204485913_gtmpl_44f242991d48f5_4x6_front.pdf",
#     "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/613ba39c6c92493d37b94bc4_4x6%20Retail%20front.pdf"
# ]

# # Links for QR codes
# links = [
#     "https://example.com/promo-1",
#     "https://example.com/promo-2"
# ]

# Example HTML templates for the front of the postcards
html_front_templates = [
    "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/5eb8636a79f886f204485913_gtmpl_44f242991d48f5_4x6_front.pdf",
    "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/613ba39c6c92493d37b94bc4_4x6%20Retail%20front.pdf",
    "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/5eb8617e074356eea7fd19ea_gtmpl_2aac2ec6d39026_4x6_front.pdf"
]

# Links for QR codes
links = [
    "https://example.com/promo-1",
    "https://example.com/promo-2",
    "https://example.com/promo-3"
]


# Function to generate a QR code as base64
def generate_qr_code(link):
    qr = qrcode.make(link)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return f"data:image/png;base64,{base64.b64encode(buffer.read()).decode('utf-8')}"

# Generate QR codes dynamically
qr_codes = [generate_qr_code(link) for link in links]

# HTML back template
html_back_template = """
<html>
  <body>
    <div style="padding: 20px; font-family: Arial, sans-serif;">
      <p>Hello {{name}}</p>
      <div style="margin-top: 20px;">
        <img src="{{qr_code_url}}" alt="QR Code" style="width: 150px; height: 150px;">
      </div>
    </div>
  </body>
</html>
"""
