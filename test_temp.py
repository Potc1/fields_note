from send_requests import getField
import pytest

def test_get_fields():
    user = '5775480864' 
    result = getField("", user)
    assert result != None
