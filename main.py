import os
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = 'C:\\Users\\Pythadela\\Downloads'

dest_dir_sfx = 'C:\\Users\\Pythadela\\Desktop\\Downloads\\Sound'
dest_dir_music = 'C:\\Users\\Pythadela\\Desktop\\Downloads\\Music'
dest_dir_video = 'C:\\Users\\Pythadela\\Desktop\\Downloads\\Video'
dest_dir_image = 'C:\\Users\\Pythadela\\Desktop\\Downloads\\Images'
dest_dir_documents = 'C:\\Users\\Pythadela\\Desktop\\Downloads\\Documents'


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):
        pass

    def check_video_files(self, entry, name):
        pass

    def check_image_files(self, entry, name):
        pass

    def check_document_files(self, entry, name):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
