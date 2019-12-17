import random

class Task:
    def __init__(self, time, average_pages):
        self.timestamp = time
        self.pages = random.randrange(1, average_pages + 1)

    def get_stamp(self):
        return self.timestamp
    
    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp
