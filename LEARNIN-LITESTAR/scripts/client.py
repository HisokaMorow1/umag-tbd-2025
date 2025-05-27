import httpx

BASE_URL = "http://localhost:8000"
USERNAME = "admin6"
PASSWORD = "admin"

def main():
    token = get_token()

    with httpx.Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {token}"}) as client:
        r = client.get("/items")
        for item in r.json():
            print(f"id = {item['id']}, title = {item['title']}, done = {item['done']}")
        new_item = add_todo(client, "nuevo todo", tags=["example", "test"], done=False)
        print(f"nuevo item agregado: {new_item}")

        if "id" in new_item:
            item = get_item(client, new_item["id"])
            print(f"item obtenido: {item}")

            updated_item = update_item(client, new_item["id"], "todo actualizado", True)
            print(f"item actualizado: {updated_item}")

            if delete_item(client, new_item["id"]):
                print("item eliminado exitosamente.")


def get_token() -> str:
    with httpx.Client(base_url=BASE_URL) as client:
        r = client.post("/auth/login", data={"username": USERNAME, "password": PASSWORD})
        r_data = r.json()
    return r_data["access_token"]

def add_todo(client, title: str, tags: list = None, done: bool = False):
    if tags is None:
        tags = []
    formatted_tags = [{"id": index, "name": tag} for index, tag in enumerate(tags)]
    response = client.post("/items", json={"title": title, "tags": formatted_tags, "done": done})
    return response.json()

def get_item(client, item_id: int):
    response = client.get(f"/items/{item_id}")
    return response.json()

def delete_item(client, item_id: int):
    response = client.delete(f"/items/{item_id}")
    return response.status_code == 204

def update_item(client, item_id: int, title: str, done: bool):
    response = client.patch(f"/items/{item_id}", json={"title": title, "done": done})
    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "detail": response.json().get("detail", "Error desconocido")}

if __name__ == "__main__":
    main()