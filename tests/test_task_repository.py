from app.repositories.task_repository import fetch_all_tasks


def test_fetch_all_tasks():
    tasks = fetch_all_tasks()
    assert len(tasks) > 0
    assert isinstance(tasks[0], dict)
    assert "id" in tasks[0]
    assert "name" in tasks[0]
