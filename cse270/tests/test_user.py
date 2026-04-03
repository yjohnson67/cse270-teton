import requests
 
def test_users_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
 
    mocker.patch("requests.get", return_value=mock_response)
 
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"
    response = requests.get(url)
 
    assert response.status_code == 200
 
 
def test_users_unauthorized(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {}
 
    mocker.patch("requests.get", return_value=mock_response)
 
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"
    response = requests.get(url)
 
    assert response.status_code == 401