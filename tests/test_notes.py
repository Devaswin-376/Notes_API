import random
def test_create_note(client):
    email = f"pytest{random.randint(1,10000)}@example.com"
    
    register = client.post("/auth/register", json={
        "email": email,
        "password": "password123"
    })
    assert register.status_code in (200, 201)
    
    login = client.post("/auth/login", data={
        "username" : email,
        "password": "password123"
    })
    assert login.status_code == 200
    assert "access_token" in login.json()
    
    token = login.json()["access_token"]
    
    res = client.post(
        "/notes/",
        json={"title" : "Test Note", "content" : "Testing"},
        headers={"Authorization" : f"Bearer {token}"}
    )
    
    assert res.status_code == 201