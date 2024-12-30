import qrcode
import io
import base64

# Example HTML template for the front of the postcard with a placeholder for the name
html_front_template_1 = "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/5eb8636a79f886f204485913_gtmpl_44f242991d48f5_4x6_front.pdf"

html_front_template_2 = "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/613ba39c6c92493d37b94bc4_4x6%20Retail%20front.pdf"

# Links for A/B testing
link_a = "https://example.com/promo-a"
link_b = "https://example.com/promo-b"

# Function to generate a QR code as base64
def generate_qr_code(link):
    qr = qrcode.make(link)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return f"data:image/png;base64,{base64.b64encode(buffer.read()).decode('utf-8')}"

# Generate QR codes for each link
qr_code_a = generate_qr_code(link_a)
qr_code_b = generate_qr_code(link_b)

# HTML templates
html_back_template_a = """
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

html_back_template_b = """
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

# Replace QR code placeholders
# html_back_template = html_back_template_1.replace("{{qr_code_url}}", qr_code_a)
html_back_template_1 = html_back_template_a.replace("{{qr_code_url}}", qr_code_a)
html_back_template_2 = html_back_template_b.replace("{{qr_code_url}}", qr_code_b)

# Print or save the rendered HTML
print("Postcard for Promo A:")
print(html_back_template_1)
print(html_back_template_2)