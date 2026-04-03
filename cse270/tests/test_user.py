import requests


def test_user_endpoint():
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        # This prevents the test from crashing if server isn't running
        assert False, "Could not connect to the server. Is Django running?"

    # Check status code
    assert response.status_code == 200

    # Check response contains expected content
    assert "admin" in response.text.lower()