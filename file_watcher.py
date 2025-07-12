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
            elif event.src_path.endswith('.cpp'):
                self.move_file(event.src_path, "Game/src/")
            else:
                print(f"Ignoring file: {event.src_path}")
    def move_file(self,source,destination):
        time.sleep(3)
        name_file = os.path.basename(source)
        destination_path = os.path.join(destination, name_file)
        shutil.move(source, destination_path)
        print(f"Moved file : {name_file} to {destination_path}")


print("=== Starting file watcher ===")
print("To stop press Ctrl+C")

manager = EventManager()

observer = Observer()
observer.schedule(manager,"build/Game/", recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("=== Stopping file watcher ===")
observer.join()


