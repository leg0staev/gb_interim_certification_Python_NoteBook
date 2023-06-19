import json
import datetime


class Note:
	def __init__(self, title: str, body: str):
		self.id = 1
		self.title = title
		self.body = body
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()

	def get_id(self) -> int:
		return self.id

	def set_id(self, new_id: int)-> None:
		self.id = new_id

	def get_title(self) -> str:
		return self.title

	def get_body(self) -> str:
		return self.body
