import unittest
from todo import Task, ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Write unit tests")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].description, "Write unit tests")

    def test_mark_task_done(self):
        self.todo_list.add_task("Write unit tests")
        self.assertTrue(self.todo_list.mark_task_done(0))
        self.assertTrue(self.todo_list.tasks[0].is_done)

    def test_mark_task_done_invalid_index(self):
        self.todo_list.add_task("Write unit tests")
        self.assertFalse(self.todo_list.mark_task_done(1))

    def test_list_tasks(self):
        self.todo_list.add_task("Write unit tests")
        self.todo_list.add_task("Learn Python")
        expected_output = "Write unit tests - Not Done\nLearn Python - Not Done"
        self.assertEqual(self.todo_list.list_tasks(), expected_output)

if __name__ == '__main__':
    unittest.main()
