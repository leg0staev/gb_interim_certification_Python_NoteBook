from Core.Models.Note import Note


class Notebook:
	def __init__(self):
		self.notes_list: list[Note] = []
		self.db_file_name: str = 'notes_db.json'

	def add_note(self, note: Note) -> None:
		if len(self.notes_list) == 0:
			self.notes_list.append(note)
		else:
			note.set_id(self.notes_list[-1].get_id() + 1)
			self.notes_list.append(note)

	def get_note_by_idx(self, idx: int) -> Note | None:
		for note in self.notes_list:
			if note.get_id() == idx:
				return note
		return None
