import requests, json, jsonpath


def test_Add_new_data():
    # Add new student
    App_URL = "http://localhost:5000/users"
    payload = {"name": "morpheus", "id": "1"}
    r = requests.post(App_URL, data=payload)
    if r.status_code == 200:
        data= json.loads(r.text)
        id = data['id']
        name = data['name']
        print("Success add data: id -> {} and name {}".format(id, name))
    else:
        print("Failed with {} Code".format(r.status_code))

def test_Get_user():
    App_URL = "http://localhost:5000/users/1"
    r = requests.get(App_URL)
    if r.status_code == 200:
        data = json.loads(r.text)
        id = data['id']
        name = data['name']
        print("Success add data: id -> {} and name {}".format(id, name))
    else:
        print("Failed with {} Code".format(r.status_code))

def test_Get_users():
    App_URL = "http://localhost:5000/users"
    r = requests.get(App_URL)
    if r.status_code == 200:
        data = json.loads(r.text)
        print(data)
    else:
        print("Failed with {} Code".format(r.status_code))

def test_Update_new_data():
    # Update new student
    App_URL = "http://localhost:5000/users/1"
    payload = {"name": "Morphius2", "id": "1"}
    r = requests.put(App_URL, data=payload)
    if r.status_code == 200:
        data = json.loads(r.text)
        id = data['id']
        name = data['name']
        print("Success add data: id -> {} and name {}".format(id, name))
    else:
        print("Failed with {} Code".format(r.status_code))

def test_Delete_new_data():
    # Delete new student
    App_URL = "http://localhost:5000/users/1"
    r = requests.delete(App_URL) # Test Delete User
    if r.status_code == 200:
        print("Success delete data")
    else:
        print("Failed with {} Code".format(r.status_code))
    # Display Data
    App_URL2 = "http://localhost:5000/users"
    rr = requests.get(App_URL2)
    data = json.loads(rr.text)
    print(data)

#pytest -v -s testCases/test_minute.py





