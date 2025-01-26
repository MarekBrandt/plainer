from app.models.task import Task, TaskInput
from app.repositories.task_repository import fetch_all_tasks, add_task, delete_task, get_task_by_id


def test_fetch_all_tasks(mocker):
    tasks = [Task(id=1, name="Task 1"), Task(id=2, name="Task 2")]
    mocker.patch('app.repositories.task_repository.mock_db', tasks)
    result = fetch_all_tasks()
    assert len(result) == 2
    assert isinstance(result[0], Task)
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[0].name == 'Task 1'
    assert result[1].name == 'Task 2'

def test_add_task_when_no_tasks(mocker):
    task_input = TaskInput(name='Task 1')
    expected_task = Task(id=0, name="Task 1")

    mocker.patch('app.repositories.task_repository.mock_db', [])
    result = add_task(task_input)

    assert isinstance(result, Task)
    assert result == expected_task

def test_added_task_has_next_id_than_last_element(mocker):
    task_input = TaskInput(name='Task 4')
    mock_db = [Task(id=0, name="Task 1"), Task(id=2, name="Task 2")]
    expected_task = Task(id=3, name="Task 4")

    mocker.patch('app.repositories.task_repository.mock_db', mock_db)
    result = add_task(task_input)

    assert isinstance(result, Task)
    assert result == expected_task

def test_get_task_by_id(mocker):
    mock_db = [Task(id=0, name="Task 1"), Task(id=2, name="Task 2")]
    expected_task = Task(id=2, name="Task 2")

    mocker.patch('app.repositories.task_repository.mock_db', mock_db)
    result = get_task_by_id(2)

    assert isinstance(result, Task)
    assert result == expected_task

def test_get_task_by_id_returns_none_when_not_found(mocker):
    mock_db = [Task(id=0, name="Task 1"), Task(id=2, name="Task 2")]

    mocker.patch('app.repositories.task_repository.mock_db', mock_db)
    result = get_task_by_id(1)

    assert result is None

def test_delete_task(mocker):
    mock_db = [Task(id=0, name="Task 1"), Task(id=2, name="Task 2")]
    expected_task = Task(id=2, name="Task 2")

    mocker.patch('app.repositories.task_repository.mock_db', mock_db)
    result = delete_task(2)

    assert isinstance(result, Task)
    assert result == expected_task
    assert len(mock_db) == 1
    assert mock_db[0].id == 0

