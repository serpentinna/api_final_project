from locust import HttpUser, between, task

from faker import Faker

from methods.folders_methods import get_first_folder_id

fake = Faker()

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
url = os.getenv("CLICKUP_API_URL")
space_id = os.getenv("SPACE_ID")
headers = {"Authorization": token}
folder_id = get_first_folder_id()


class WebsiteUser(HttpUser):
    wait_time = between(2, 5)

    # def on_start(self):
    #     created_folder_name = {"name": fake.name()}
    #     self.client.post(
    #         f"/api/v2/space/{space_id}/folder",
    #         headers=headers,
    #         json=created_folder_name
    #     )

    @task
    def get_folder(self):
        self.client.get(
            f"/api/v2/folder/{folder_id}",
            headers=headers)

    @task
    def update_folder(self):
        updated_folder_name = {"name": fake.name()}
        self.client.put(
            f"/api/v2/folder/{folder_id}",
            headers=headers,
            json=updated_folder_name
        )