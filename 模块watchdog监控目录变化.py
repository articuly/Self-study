# coding:utf-8
from watchdog.observers import Observer
from watchdog.events import *
import time


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f'{now} DIR move from {event.src_path} to {event.dest_path}')
        else:
            print(f'{now} FILE move from {event.src_path} to {event.dest_path}')

    def on_created(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f'{now} DIR {event.src_path} created')
        else:
            print(f'{now} FILE {event.src_path} created')

    def on_deleted(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f'{now} DIR {event.src_path} deleted')
        else:
            print(f'{now} FILE {event.src_path} deleted')

    def on_modified(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f'{now} DIR {event.src_path} modified')
        else:
            print(f'{now} FILE {event.src_path} modified')


if __name__ == '__main__':
    observer = Observer()
    path = r'E:\Downloads'
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path, recursive=True)
    print(f'Observing {path}')
    observer.start()
    observer.join()
