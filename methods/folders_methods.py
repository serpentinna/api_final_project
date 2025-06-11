from faker import Faker

fake = Faker()

import requests

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
url = os.getenv("CLICKUP_API_URL")
space_id = os.getenv("SPACE_ID")
headers = {"Authorization": token}

def create_folder():
    folder_name = {"name": fake.name()}
    return requests.post(url + f"space/{space_id}/folder", headers=headers, json=folder_name)

def get_all_folders():
    return requests.get(url+f"space/{space_id}/folder", headers=headers)

def get_folder():
    result = get_all_folders()
    first_folder_id = result.json()["folders"][0]["id"]
    return requests.get(url+"folder/"+first_folder_id, headers=headers)

def update_folder():
    result = create_folder()
    created_folder_id = result.json()["id"]
    assert result.status_code == 200
    assert result.json()["id"] == created_folder_id
    updated_folder_name = {"name": fake.name()}
    result = requests.put(url + "folder/" + created_folder_id, headers=headers, json=updated_folder_name)
    assert result.status_code == 200
    assert result.json()["name"] == updated_folder_name["name"]
    result = requests.delete(url + "folder/" + created_folder_id, headers=headers)
    assert result.status_code == 200
    return requests.delete(url + "folder/" + created_folder_id, headers=headers)

def delete_folder():
    result = get_all_folders()
    first_folder_id = result.json()["folders"][0]["id"]
    assert result.status_code == 200
    return requests.delete(url + "folder/" + first_folder_id, headers=headers)

def get_first_folder_id():
    result = get_all_folders()
    first_folder_id = result.json()["folders"][0]["id"]
    return first_folder_id