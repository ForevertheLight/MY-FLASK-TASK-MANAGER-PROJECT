# Import the Flask class and the request object from the flask module
# Flask is used to create the web application, while request handles incoming HTTP data
from flask import Flask, request

# Import various validation helper functions from the 'utils.validators' module
# These functions help ensure that incoming user data meets specific requirements
from utils.validators import (
    validate_payload,          # Ensures that the request payload exists and is valid JSON
    validate_required_fields,  # Checks that specific fields are present in the payload
    validate_field_length,     # Ensures that certain fields meet the minimum character length
    validate_email,            # Validates the format of the email address
    validate_phone,            # Validates the phone number for correct digits and prefix
    validate_unique_field      # Ensures that fields like email and phone are unique
)

# Import response helper functions from the 'utils.response' module
# These standardize the structure and format of API responses
from utils.response import (
    make_response,             # Builds a standardized response object
    success_response,          # Generates a success message response (HTTP 200)
    bad_request_response,      # Generates an error response for invalid requests (HTTP 400)
    not_found_response,        # Generates an error response for missing resources (HTTP 404)
    internal_error_response,   # Generates an error response for server errors (HTTP 500)
    format_response            # Formats data before sending it in the response
)

# Initialize a Flask application instance
# '__name__' tells Flask where to find resources like templates and static files
app = Flask(__name__)

# Create in-memory dictionaries to act as simple databases
# 'users' will store user records, and 'tasks' will store task records
users = {}
tasks = {}

# Initialize auto-incrementing ID counters for users and tasks
# These help generate unique IDs for each new user or task
next_user_id = 1
next_task_id = 1

# Define a sample user model structure for reference
# Each user record must include an ID, first name, last name, email, and phone number
user = {
    'id': 1,
    'firstName': 'Joshua',
    'lastName': 'Fashola',
    'email': 'fashjosh2004@gmail.com',
    'phone': '08160840249'
}

# Define an API endpoint for creating a new user
# The route '/api/v1/user/add' listens for HTTP POST requests
@app.route('/api/v1/user/add', methods=['POST'])
def create_user():
    # Use 'global' to access and modify the global 'next_user_id' variable
    global next_user_id

    # Retrieve the incoming JSON data from the client request body
    data = request.get_json()

    # Validate that the JSON payload exists and is properly formatted
    payload = validate_payload(data)
    if payload:
        # If validation fails, return a 400 Bad Request response with the error message
        return bad_request_response(payload)

    # Validate all required fields and check field lengths
    # Each validation function returns an error message if validation fails
    error = (validate_required_fields(data, 'firstName') or 
             validate_required_fields(data, 'lastName') or 
             validate_required_fields(data, 'email') or 
             validate_required_fields(data, 'phone') or 
             validate_field_length(data, 'firstName') or 
             validate_field_length(data, 'lastName'))
    if error:
        # If any required field or length check fails, return a 400 Bad Request
        return bad_request_response(error)

    # Validate that the provided email has a valid format
    if not validate_email(data['email']):
        return bad_request_response("Invalid email format")
    
    # Validate the phone number for correct format, length, and prefix
    if not validate_phone(data['phone']):
        return bad_request_response(
            "Phone number must be numeric and at least 11 digits long "
            "starting with a valid prefix (070, 080, 090, 081, 091)"
        )
    
    # Ensure the provided email address is unique among existing users
    if not validate_unique_field(users, 'email', data['email']):
        return bad_request_response(f"User with email '{data['email']}' already exists")
    
    # Ensure the provided phone number is unique among existing users
    if not validate_unique_field(users, 'phone', data['phone']):
        return bad_request_response(f"User with phone number '{data['phone']}' already exists")
    
    # Create a new user dictionary with validated input data
    user = {
        'id': next_user_id,
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'email': data['email'],
        'phone': data['phone']
    }
    
    # Add the new user record to the 'users' dictionary using the next available ID
    users[next_user_id] = user

    # Increment the user ID counter for the next new user
    next_user_id += 1
    
    # Return a success response with formatted user data and HTTP 201 (Created)
    return success_response("User created successfully", format_response(user, 'user'), 201)
