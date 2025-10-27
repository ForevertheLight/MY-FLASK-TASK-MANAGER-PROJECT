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

# Format a list of user objects for consistent API response structure
def format_users(users):
    # Use a list comprehension to loop through each user in the 'users' list
    # Call the 'format_user' function on each user to format their details
    # Return a new list containing all formatted user dictionaries
    return [format_user(user) for user in users]

# Format a list of task objects for consistent API response structure
def format_tasks(tasks):
    # Use a list comprehension to iterate through each task in the 'tasks' list
    # Call the 'format_task' function on each task to format its details
    # Return a new list containing all formatted task dictionaries
    return [format_task(task) for task in tasks]

# Generate a standardized success response for API requests
def success_response(message, data=None, status_code=200):
    # Call the 'make_response' function to build a response object
    # The first argument "success" indicates the response status
    # 'message' provides a success message describing the outcome
    # 'data' holds any additional information or payload (default is None)
    # 'status_code' represents the HTTP status code (default is 200 for OK)
    return make_response("success", message, data, status_code)

# Generate a standardized "not found" error response for missing resources
def not_found_response(message="Resource not found"):
    # Call the 'make_response' function to build an error response object
    # The first argument "error" indicates the response status
    # 'message' provides a description of the error (default is "Resource not found")
    # The 'data' field is set to None since no resource data is returned
    # The HTTP status code 404 indicates that the requested resource was not found
    return make_response("error", message, None, 404)

# Generate a standardized "bad request" error response for invalid client requests
def bad_request_response(message="Bad request"):
    # Call the 'make_response' function to build an error response object
    # The first argument "error" indicates that the request failed
    # 'message' provides a description of the error (default is "Bad request")
    # The 'data' field is set to None because no valid data is returned
    # The HTTP status code 400 represents a client-side error (bad request)
    return make_response("error", message, None, 400)

