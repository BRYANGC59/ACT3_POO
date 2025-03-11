class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id:int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        self.tag: str = tag
        if self.tag is not self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self. code_id} - {self.title}"

class TodoBook:

    def __init__(self):
        self.todos = {}

    def add_todo(self, title: str, description:str) -> int:
        total_id = len(self.todos) +1
        objeto_todo = Todo(total_id, title, description)
        self.todos.(total_id, objeto_todo)

        return total_id in objeto_todo




