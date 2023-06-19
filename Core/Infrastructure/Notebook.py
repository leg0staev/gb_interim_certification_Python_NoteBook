from Core.Models.Note import Note


class Notebook:
	notes_list: list[Note] = []

	def add_note(self, note: Note) -> None:
		if len(self.notes_list) == 0:
			self.notes_list.append(note)
		else:
			note.set_id(len(self.notes_list) + 1)
			self.notes_list.append(note)

	def get_note_by_idx(self, idx: int) -> Note | None:
		for note in self.notes_list:
			if note.get_id() == idx:
				return note
		return None
