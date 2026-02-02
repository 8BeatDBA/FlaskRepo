#test_app.py 

from app import app

def test_home():
    # Create a test client
    client = app.test_client()
    
    # Make a GET request to the homepage
    response = client.get("/main")
    
    # Check that the response data matches
    assert response.data == b"Server is up and running! Listening for requests.. "
    
    # Check that the status code is 200 (OK)
    assert response.status_code == 200
    

def test_data_post():
    client = app.test_client()
    
    # Send a POST request with JSON
    response = client.post("/data", json={"item": "book"})
    
    # Assert status is 200 (Created)
    assert response.status_code == 200
    
    # Assert the response body contains what we expect
    # assert response.data == b"Received: book"