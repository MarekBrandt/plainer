from app.models.task import Task, TaskInput
import app.repositories.task_repository as tr


def get_all_tasks() -> list[Task]:
    tasks = tr.fetch_all_tasks()
    return tasks


def create_task(task: TaskInput) -> Task:
    if not task.name:
        raise ValueError("Name cannot be empty")
    return tr.add_task(task)

def delete_task(task_id: int) -> Task:
    return tr.delete_task(task_id)
