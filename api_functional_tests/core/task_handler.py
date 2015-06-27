import requests
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
del path

import config

class TaskHandler():
	@classmethod
	def get_tasks(cls, username, password):
		r= requests.get(url=config.API_URL+config.TASKS_TAIL, auth=(username, password))
		print(r.status_code)
		print(r.text)

if __name__ == '__main__':
	print(TaskHandler.get_tasks(config.DEFAULT_USERNAME, config.DEFAULT_PASSWORD))
