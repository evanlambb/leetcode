import copy

class TextEditor:
    def __init__(self):
        # Maps file_id (str) to a list of lines (list[str])
        self.files = dict()
        # Maps version_id (int) to a saved snapshot of self.files
        self.versions = dict()

    def create_file(self, file_id: str) -> bool:
        if file_id in self.files:
            return False
        self.files[file_id] = []
        return True

    def append_line(self, file_id: str, text: str) -> bool:
        if file_id not in self.files:
            return False
        self.files[file_id].append(text)
        return True

    def get_file_contents(self, file_id: str) -> list[str]:
        if file_id not in self.files:
            return []
        return self.files[file_id]

    def save_version(self, version_id: int) -> None:
        # Save the complete state of self.files at this exact moment
        self.versions[version_id] = {
          'files' : copy.deepcopy(self.files)
        }

    def restore_version(self, version_id: int) -> bool:
        # Restore self.files to the exact state saved at version_id
        # Return True if successful, False if version_id doesn't exist
        if version_id not in self.versions:
          return False
          
        v = self.versions[version_id]
        self.files = copy.deepcopy(v['files'])

# --- Test Execution ---
editor = TextEditor()

editor.create_file("notes.txt")
editor.append_line("notes.txt", "Meeting at 10 AM")

editor.save_version(1)

editor.append_line("notes.txt", "Buy milk")
editor.create_file("todo.txt")

editor.restore_version(1)

print("Notes contents:", editor.get_file_contents("notes.txt")) 
# EXPECTED: ['Meeting at 10 AM']

print("Todo contents:", editor.get_file_contents("todo.txt")) 
# EXPECTED: []