import pytest
from filter import filter

def testInputType():
    with pytest.raises(TypeError) as typeException:
        raise TypeError('This function only works with strings. Input a string and try again.')