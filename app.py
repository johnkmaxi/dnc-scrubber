# Import Flask and other modules
from flask import Flask, request, render_template, send_file
import os
import subprocess

# Create a Flask app object
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the home.html template
    return render_template('home.html')

# Define the route for the upload page
@app.route('/upload', methods=['POST'])
def upload():
    # Get the file from the request
    file = request.files['file']
    # Save the file to a temporary location
    file.save('temp.csv')
    # Execute the Python script on the file
    output = subprocess.check_output(['python', 'script.py', 'temp.csv'])
    # Delete the temporary file
    os.remove('temp.csv')
    # Render the upload.html template with the output
    return send_file('output.csv', as_attachment=True)

# Run the app
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
