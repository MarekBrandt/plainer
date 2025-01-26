from app.models.task import Task, TaskInput

mock_db: list[Task] = [Task(id=1, name="Task 1"), Task(id=2, name="Task 2")]


def fetch_all_tasks() -> list[Task]:
    return mock_db

def get_task_by_id(task_id: int) -> Task | None:
    for task in mock_db:
        if task.id == task_id:
            return task
    return None

def add_task(task: TaskInput) -> Task:
    max_id = -1
    if len(mock_db) != 0:
        max_id = mock_db[-1].id
    next_id = max_id + 1

    new_task = Task(id=next_id, name=task.name)
    mock_db.append(new_task)
    return new_task

def delete_task(task_id: int) -> Task:
    task = get_task_by_id(task_id)
    mock_db.remove(task)
    return task
