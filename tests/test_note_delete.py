def test_note_delete(client):
    email = "test@example.com"
    password = "password123"
    
    login = client.post("/auth/login", data={
        "username" : email,
        "password" : password
    })
    
    token = login.json()["access_token"]
    
    headers = {"Authorization" : f"Bearer {token}"}
    # Create a note to delete
    res = client.post("/notes/", json={
        "title" : "Note to delete",
        "content" : "This note will be deleted"
    }, headers=headers)
     
    note_id = res.json()["id"]
    
    res = client.delete(f"/notes/{note_id}", headers=headers)
    assert res.status_code == 200
    
    