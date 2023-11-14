from fastapi import HTTPException
from helpers.utils import validate_uuid
from uuid import UUID

def test_valid_uuid():
    # Test with a valid UUID
    uuid_str = "550e8400-e29b-41d4-a716-446655440000"
    result = validate_uuid(uuid_str)
    assert isinstance(result, UUID)

def test_invalid_uuid():
    # Test with an invalid UUID
    invalid_uuid_str = "not_a_valid_uuid"
    try:
        validate_uuid(invalid_uuid_str)
    except HTTPException as e:
        assert e.status_code == 400
        assert str(e.detail) == "Invalid UUID format"
    else:
        # Fail the test if no exception is raised
        assert False, "Expected HTTPException, but no exception was raised"
