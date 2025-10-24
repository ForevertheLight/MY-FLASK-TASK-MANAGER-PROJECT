import re
#'re' stands for regular expressions 
#It allows you to 'search','match','validate',or'replace' text patterns inside strings.
#For example,checking if a name only contains letters, 
# or if a password meets certain complexity rules.

# Payload validation
def validate_payload(payload):
    #Checks if payload is supplied by the user
    if payload is None:
        return "Payload is missing"
    #Checks if payload is a Dictionary datatype
    if not isinstance(payload, dict):
        return "Payload must be a valid JSON object"
    #Checks if payload is not empty
    if not payload:
        return "Payload cannot be empty"
    return None

# Ensure input field is present and non-empty in the payload
def validate_required_fields(data, field):
    #Checks if  'Keys' exist in payload and ensure the 'value' is not empty
    if field not in data or not str(data[field]).strip():
        return f"{field.capitalize()} is required and cannot be empty"
    return None