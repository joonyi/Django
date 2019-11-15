import requests

URL = "http://localhost:8000"

def get_token():
    # Get auth token
    url = f"{URL}/api/auth/"
    response = requests.post(url, data={'username': 'admin', 'password': '123'})
    return response.json()


def get_data():
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    job_seeker_data = response.json()
    for e in job_seeker_data:
        print(e)


def create_new(count):
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "job_seeker_id": f"HQ00{count}",
        "name": "Koh",
        "ranking": 5,
        "age": 29,
    }
    response = requests.post(url, data=data, headers=header)
    print(response.text)


def edit_data(job_seeker_id):
    url = f"{URL}/api/users_list/{job_seeker_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "name": "Koh",
        "ranking": 2.8,
        "age": 29,
    }
    response = requests.put(url, data=data, headers=header)
    print(response.text, response.status_code)


def delete_data(job_seeker_id):
    url = f"{URL}/api/users_list/{job_seeker_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    print(response.status_code)

get_data()