from uuid import UUID
from fastapi import HTTPException

def validate_uuid(uuid_str: str) -> UUID:
    """
    Validate a string and convert it to a UUID.
    
    Args:
        uuid_str (str): The input string to validate and convert.
        
    Returns:
        UUID: The converted UUID.
        
    Raises:
        HTTPException: If the input string is not a valid UUID format.
    """
    try:
        validated_uuid = UUID(uuid_str)
    except ValueError:
        print("DEBUG: Invalid UUID format")
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    return validated_uuid
