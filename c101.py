from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route and handler for processing form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    # Access form data submitted by the user
    name = request.form['name']
    email = request.form['email']

    # Process the form data (e.g., save to database, send email, etc.)
    # Your code to process the form data goes here

    # Redirect the user to a thank-you page
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
