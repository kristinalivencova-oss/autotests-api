import httpx


payload = {
"email": "kristina2@test.com",
        "password": "Kristina123"
    }

response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=payload)
print(response.status_code)
print(response.json())




access_token = response.json()["token"]["accessToken"]

response = httpx.get("http://localhost:8000/api/v1/users/me",
            headers= {"Authorization": f"Bearer {access_token}"})

print(response.status_code)
print(response.json())