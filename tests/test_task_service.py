import pytest

from app.models.task import Task, TaskInput
from app.services.task_service import get_all_tasks, create_task


def test_get_all_tasks(mocker):
    mock_tasks = [
        Task(id=1, name='Task 1'),
        Task(id=2, name='Task 2'),
    ]

    mocker.patch('app.services.task_service.fetch_all_tasks', return_value=mock_tasks)

    tasks = get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].name == "Task 1"
    assert tasks[0].id == 1
    assert tasks[1].name == "Task 2"
    assert tasks[1].id == 2


def test_post_task(mocker):
    taskInput = TaskInput(name='Task 1')
    mock_task = Task(id=1, name='Task 1')

    mocker.patch('app.services.task_service.add_task', return_value=mock_task)

    result = create_task(taskInput)
    assert result == mock_task


def test_post_task_raises_exception_when_no_name():
    taskInput = TaskInput(name='')

    with pytest.raises(ValueError):
        create_task(taskInput)
