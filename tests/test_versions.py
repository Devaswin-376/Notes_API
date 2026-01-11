import random

def test_note_version(client):
    email = f"pytest{random.randint(1,10000)}@example.com"
    password = "password123"
    
    client.post("/auth/register", json={
        "email" : email,
        "password" : password
        })
    
    login = client.post("/auth/login", data={
        "username" : email,
        "password" : password
    })
    token = login.json()["access_token"]
    
    headers = {"Authorization" : f"Bearer {token}"}
    
    #creating note (version 1)
    res = client.post(
        "/notes/",
        json={
            "title" : "Version Note",
            "content" : "Initial content"
        },
        headers = headers
    )
    
    note_id = res.json()["id"]
    
    #Update note (version 2)
    client.put(
        f"/notes/{note_id}",
        json={
            "title" : "Version Note",
            "content" : "Updated Initial content"
        },
        headers=headers
    )
    
    versions = client.get(
        f"/notes/{note_id}/versions",
        headers=headers 
    )
    
    assert versions.status_code == 200
    assert len(versions.json()) == 2
    