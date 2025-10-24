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
