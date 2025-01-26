from dataclasses import dataclass


@dataclass
class Task:
    id: int
    name: str

@dataclass
class TaskInput:
    name: str