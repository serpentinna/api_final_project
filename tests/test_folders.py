from methods.folders_methods import create_folder, get_all_folders, get_folder, update_folder, delete_folder

def test_create_folder():
    result = create_folder()
    created_folder_id = result.json()["id"]
    assert result.status_code == 200
    assert result.json()["id"] == created_folder_id


def test_get_all_folders():
    result = get_all_folders()
    first_folder_id = result.json()["folders"][0]["id"]
    assert result.status_code == 200
    assert result.json()["folders"][0]["id"] == first_folder_id

def test_get_folder():
    result = get_folder()
    folder_id = result.json()["id"]
    assert result.status_code == 200
    assert result.json()["id"] == folder_id

def test_update_folder():
    result = update_folder()
    assert result.status_code == 200


def test_delete_folder():
    result = delete_folder()
    assert result.status_code == 200