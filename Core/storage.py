from pathlib import Path

from django.core.files.storage import FileSystemStorage

class ExistStorage(FileSystemStorage):
    """
    Returns same name for existing file and deletes existing file on save.
    """
    def _save(self, name, content):
        print(*vars(self).items(), sep = "\n")
        if self.exists(name):
           return name
        return super(ExistStorage, self)._save(name, content)

    def get_available_name(self, name,max_length=None):
        return name