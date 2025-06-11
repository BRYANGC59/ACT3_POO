class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed = False
        self.tags = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f'{self.code_id} - {self.title}'

class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) ->int:
        new_id = len(self.todos) +1
        new_todo = Todo(new_id, title, description)
        self.todos[new_id] = new_todo
        return new_id

    def pending_todos(self) ->[Todo]:
        pending = [element for element in self.todos.values() if not element.completed]
        return pending

    def completed_todos(self) -> [Todo]:
        ready = [element for element in self.todos.values() if element.completed]
        return ready

    def tags_todo_count(self) -> {str, int}:
        account = {}
        for element in self.todos.values():
            for i in element.tags:
                if i not in account:
                    account[i] = 0
                account[i] += 1
        return account