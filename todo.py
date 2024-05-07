class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        return f"{self.description} - {'Done' if self.is_done else 'Not Done'}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()
            return True
        return False

    def list_tasks(self):
        return '\n'.join(str(task) for task in self.tasks)
