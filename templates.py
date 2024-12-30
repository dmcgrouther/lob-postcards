# Example HTML template for the front of the postcard with a placeholder for the name
html_front_template_1 = "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/5eb8636a79f886f204485913_gtmpl_44f242991d48f5_4x6_front.pdf"

html_front_template_2 = "https://cdn.prod.website-files.com/5e1e5c62fa3d44c96b4170a1/613ba39c6c92493d37b94bc4_4x6%20Retail%20front.pdf"

html_front_template_3 = """
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