from app.models.task import Task


def fetch_all_tasks():
    return [
        Task(id=1, name="Task 1").to_dict(),
        Task(id=2, name="Task 2").to_dict(),
    ]