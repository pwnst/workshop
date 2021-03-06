import requests
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import config
from core.task_parser import ResponseParser

class TaskHandler():
	@classmethod
	def get_tasks(cls, task_id, username, password):
		raw_response = requests.get(url=config.API_URL+config.TASK_TAIL+str(task_id), auth=(username, password))
		return ResponseParser.get_task(raw_response)

if __name__ == '__main__':
	print(TaskHandler.get_tasks(1, config.DEFAULT_USERNAME, config.DEFAULT_PASSWORD))
