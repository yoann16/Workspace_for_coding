import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EventManager(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")
            if event.src_path.endswith('.h'):
                print(f" Is a header file")
            elif event.src_path.endswith('.cpp'):
                print(f"Is a source file")
            else:
                print(f"Ignoring file: {event.src_path}")


