import requests

URL = "HTTP://127.0.0.1:5000/users"

def update_user(id, first_name, last_name, hobbies):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": bobbies
    }
    url = URL + "/" + id
    response = requests.put(url, json-user)
    if response.status_code== 204:

if__name__ == "__main__":
    id = input("Type in the user's ID:")
    fname = input("Type in the user's first name")
    lname = input("Type in the user's last name")
    hobbies = input("Type in the user's favorite hobby")
    update_user(id, fname, lname, hobbies)
