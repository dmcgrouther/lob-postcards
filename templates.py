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