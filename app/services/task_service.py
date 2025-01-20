from app.repositories.task_repository import fetch_all_tasks

def get_all_tasks():
    tasks = fetch_all_tasks()
    return tasks