import os
import time
import shutil

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

INPUT_DIR = "./data/input"
OUTPUT_DIR = "./data/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            os.makedirs(event.src_path.replace(INPUT_DIR, OUTPUT_DIR), exist_ok=True)
        else:
            output_path = event.src_path.replace(INPUT_DIR, OUTPUT_DIR)

            print("Detected file \"", event.src_path, "\", moving to \"", output_path, "\"")

            shutil.copy2(event.src_path, output_path)

observer = Observer()
observer.schedule(MyEventHandler(), INPUT_DIR, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()