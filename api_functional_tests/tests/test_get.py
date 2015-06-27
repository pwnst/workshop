import pytest
import sys
import os

#if __name__ == '__main__':
#    sys.path.append(os.path.dirname(__file__) + '/../')
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from core.task_handler import TaskHandler
from config import DEFAULT_PASSWORD as PASSWORD
from config import DEFAULT_USERNAME as USERNAME

def parametrize_id():
	return pytest.mark.parametrize("task_id, expected_title", [(1, 'Buy groceries'), (2, 'Learn Python'), (3, 'Learn Java8')],
			ids=['First task', 'Second task', 'Third task'])

class TestGetMethod:
	@classmethod
	def setup_class(cls):
		cls.task_handler = TaskHandler

	@parametrize_id()
	def test_get_task(self, task_id, expected_title):
		actual_task = self.task_handler.get_tasks(task_id=task_id, username=USERNAME, password=PASSWORD)
		assert actual_task.title == expected_title, 'Invalid title'
