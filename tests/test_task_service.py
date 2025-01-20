from app.services.task_service import get_all_tasks


def test_get_all_tasks(mocker):
    mock_tasks = [
        {"id": 1, "name": "Mock Task 1"},
        {"id": 2, "name": "Mock Task 2"},
    ]

    mocker.patch('app.services.task_service.fetch_all_tasks', return_value=mock_tasks)

    tasks = get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0]["name"] == "Mock Task 1"
