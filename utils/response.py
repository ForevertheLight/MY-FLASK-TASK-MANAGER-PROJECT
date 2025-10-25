# Import the datetime class and timezone object to work with date, time, and time zone information
from datetime import datetime, timezone

# Create a standardized response object
def make_response(status, message, data=None, code=200):
    # Return a dictionary representing the response body
    # 'status' indicates whether the request was successful or failed (e.g., "success" or "error")
    # 'message' provides additional information or context about the response
    # 'data' holds any optional payload or result data (default is None)
    # 'timestamp' records the current UTC time when the response was generated
    # The second return value 'code' represents the HTTP status code (default is 200)
    return {
        'status': status,
        'message': message,
        'data': data,
        'timestamp': datetime.now(timezone.utc).isoformat()
    }, code

# Format a user object for consistent API response structure
def format_user(user):
    # Return a dictionary containing the user's essential details
    # 'id' is the unique identifier for the user
    # 'firstName' is the user's given name
    # 'lastName' is the user's family name
    # 'email' is the user's email address
    # 'phone' is the user's phone number
    return {
        'id': user['id'],
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'email': user['email'],
        'phone': user['phone']
    }
