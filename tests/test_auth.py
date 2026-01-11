import random

def test_register_and_login(client):
    email = f"pytest{random.randint(1,10000)}@example.com"
    
    res = client.post("/auth/register", json={
        "email": email,
        "password": "password123"
    })
    assert res.status_code in (200, 201)
    
    res = client.post("/auth/login", data={
        "username" : email,
        "password": "password123"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()