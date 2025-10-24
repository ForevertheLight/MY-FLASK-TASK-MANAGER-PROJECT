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

# Ensure input field only accept alphabet, and a minimum length of 3 characters
def validate_field_length(data,field,min=3):
    # Checks if the value is missing from the dictionary, or if it is not an alphabet or if it is not up to three characters
     if field not in data or not (data[field].isalpha())  or len(str(data[field]).strip()) < min:
          return f"{field.capitalize()} cannot be less than {min} alphabetic characters" 
     return None