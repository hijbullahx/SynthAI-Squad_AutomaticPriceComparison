from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# This is the 'route' for homepage
@app.route('/')
def index():
    """
    Serves the main homepage (index.html).
    """
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare():
    """
    Handles the data submitted from the form.
    """
    
    service_type = request.form.get('service_type')
    location = request.form.get('location')

    print(f"User is looking for: {service_type} in {location}")

 
    return f"<h1>Searching for: {service_type} in {location}</h1>"


if __name__ == '__main__':
  
    app.run(debug=True)