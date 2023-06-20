import json
import datetime


class Note:
	def __init__(self, id: int,
						title: str,
						body: str,
						date_created: datetime,
						date_modified: datetime):
		self.id = id
		self.title = title
		self.body = body
		self.date_created = date_created
		self.date_modified = date_modified

	def get_id(self) -> int:
		return self.id

	def set_id(self, new_id: int)-> None:
		self.id = new_id

	def get_title(self) -> str:
		return self.title

	def get_body(self) -> str:
		return self.body

	def serialize(self) -> dict:
		return {
				"id": self.id,
				"title": self.title,
				"body": self.body,
				"date_created": self.date_created.isoformat(),
				"date_modified": self.date_modified.isoformat()
		}
