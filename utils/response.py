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

# Format a task object for consistent API response structure
def format_task(task):
    # Return a dictionary containing all key details about a task
    # 'id' is the unique identifier for the task
    # 'user_id' links the task to the user who owns it
    # 'title' is the name or short summary of the task
    # 'description' provides more detailed information about the task
    # 'status' indicates the current state of the task (e.g., pending, in progress, completed)
    # 'duration' specifies how long the task is expected to take or has taken
    # 'created_at' records the date and time when the task was created
    # 'updated_at' records the date and time when the task details were last modified
    # 'completed_at' records the date and time when the task was finished
    return {
        'id': task['id'],
        'user_id': task['user_id'],
        'title': task['title'],
        'description': task['description'],
        'status': task['status'],
        'duration': task['duration'],
        'created_at': task['created_at'],
        'updated_at': task['updated_at'],
        'completed_at': task['completed_at']    
    }
