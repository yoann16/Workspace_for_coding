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
                self.move_file(event.src_path, "Game/include/")
                print(f" Is a header file")
            elif event.src_path.endswith('.cpp'):
                self.move_file(event.src_path, "Game/src/")
                print(f"Is a source file")
            else:
                print(f"Ignoring file: {event.src_path}")
    def move_file(self,source,destination):
        time.sleep(3)
        name_file = os.path.basename(source)
        destination_path = os.path.join(destination, name_file)
        shutil.move(source, destination_path)


