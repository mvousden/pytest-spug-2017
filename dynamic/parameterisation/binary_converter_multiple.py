import pytest


def integer_to_binary(inputInteger, zeroPadLength=0):
    """
    Converts an integer to a zero-padded binary string.
    """
    return "{{:0{}b}}".format(zeroPadLength).format(inputInteger)


@pytest.fixture(params=range(3))
def testCase(request):
    if request.param == 0:
        testCase = {"input": 8,
                    "expectedResult": "1000"}

    elif request.param == 1:
        testCase = {"input": 0,
                    "expectedResult": "0"}

    elif request.param == 2:
        testCase = {"input": 1,
                    "expectedResult": "1"}

    return testCase


def test_my_converter(testCase):
    assert integer_to_binary(testCase["input"]) == testCase["expectedResult"]
