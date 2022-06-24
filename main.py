import os
from os.path import exists, splitext, join
from shutil import move
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


audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt",
                    ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv",
                    ".mov", ".qt", ".flv", ".swf", ".avchd"]

document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        os.rename(old_name, new_name)
    move(entry, dest)


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
