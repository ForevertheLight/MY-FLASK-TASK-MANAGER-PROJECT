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

# Ensure email format is valid
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # Use re.match to check if the email matches the pattern
    return bool(re.match(pattern, email))

# Ensure phone number is a digit and must not be less or greater than 11 digits
def valid_phone_isDigit_and_length(phone, min = 11):
     # Checks if phone number contains only numeric characters and not shorter that 11 digits
     return (phone.isdigit() and len(phone) >= min)

# Phone number should start with a valid prefix
def valid_phone_format(phone):
    #Checks if phone number starts with one of the valid prefixes in the list below.
    valid_prefixes = ['070', '080', '090', '081', '091']
    return any(phone.startswith(prefix) for prefix in valid_prefixes)

# Validate phone number by checking both its length/digit format and valid prefix
def validate_phone(phone):
     return valid_phone_isDigit_and_length(phone) and valid_phone_format(phone)



