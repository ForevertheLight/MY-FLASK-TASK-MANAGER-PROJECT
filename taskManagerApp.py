from flask import Flask,request

from utils.validators import (
    validate_payload,
    validate_required_fields,
    validate_field_length,
    validate_email,
    validate_phone,
    validate_unique_field
)

from utils.response import (
    make_response,
    success_response,
    bad_request_response,
    not_found_response,
    internal_error_response,
    format_response
)

app=Flask(__name__)

#Our in-memory databases
users={}
tasks={}

# Auto-incrementing IDs
next_user_id=1
next_task_id=1

#Creating the User Model
#A user in this system needs five things
user = {
    'id': 1,
    'firstName': 'Joshua',
    'lastName': 'Fashola',
    'email': 'fashjosh2004@gmail.com',
    'phone': '08160840249'
}


#Our First endpoint to create new user and to ensure Phone numbers and Emails are Unique
@app.route('/api/v1/user/add', methods=['POST'])
def create_user():
    global next_user_id
    data = request.get_json()

    # Validate that payload exists and is a proper JSON
    payload = validate_payload(data)
    if payload:
        return bad_request_response(payload)

    # Validate required fields
    error = (validate_required_fields(data, 'firstName') or 
             validate_required_fields(data, 'lastName') or 
             validate_required_fields(data, 'email') or 
             validate_required_fields(data, 'phone') or 
             validate_field_length(data, 'firstName') or 
             validate_field_length(data, 'lastName'))
    if error:
        return bad_request_response(error)

    # Email format validation
    if not validate_email(data['email']):
        return bad_request_response("Invalid email format")
    
    # Phone validation
    if not validate_phone(data['phone']):
        return bad_request_response("Phone number must be numeric and at least 11 digits long starting with a valid prefix (070, 080, 090, 081, 091)")
    
    # Check for duplicate email
    if not validate_unique_field(users, 'email', data['email']):
        return bad_request_response(f"User with email '{data['email']}' already exists")
    
    # Check for duplicate phone number
    if not validate_unique_field(users, 'phone', data['phone']):
        return bad_request_response(f"User with phone number '{data['phone']}' already exists")
    
    # Create the user
    user = {
        'id': next_user_id,
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'email': data['email'],
        'phone': data['phone']
    }
    
    users[next_user_id] = user
    next_user_id += 1
    
    return success_response("User created successfully", format_response(user, 'user'), 201)