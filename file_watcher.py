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
        if not os.path.exists(source):
            print(f"Source file does not exist: {source}")
            return
        if not os.path.exists(destination):
            print(f"Destination folder does not exist: {destination}")
            return
        name_file = os.path.basename(source)
        destination_path = os.path.join(destination, name_file)
        final_destination = self.find_available_name(destination_path)
        try:
            shutil.move(source, final_destination)
            print(f"Moved file : {name_file} to {final_destination}")
        except Exception as e:
            print(f"Error moving file {name_file}: {e}")
    def find_available_name(self,destination_path):
        if not os.path.exists(destination_path):
            return destination_path
        folder = os.path.dirname(destination_path)
        full_name = os.path.basename(destination_path)
        name_base,extend = os.path.splitext(full_name)

        index = 1
        while True:
            new_name = f"{name_base}({index}){extend}"
            new_path = os.path.join(folder, new_name)
            if not os.path.exists(new_path):
                return new_path
            index += 1


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


