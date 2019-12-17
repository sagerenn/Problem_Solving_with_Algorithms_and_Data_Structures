# a simulation will be helped to find the factors of problems.
# You need to find the relationship of the factors and result by using math analyzing.

from queue_adt import Queue
import random
from task import Task
from printer import Printer

def new_print_task(student_no):
    num = random.randrange(1, 3600//(student_no*2) + 1)
    if num == 3600//(student_no*2):
        return True
    else:
        return False

def simulation(student_no, average_pages, num_seconds, pagerate):

    lab_printer = Printer(pagerate)
    print_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if new_print_task(student_no):
            task = Task(current_second, average_pages)
            print_queue.enqueue(task)

        if not lab_printer.busy() and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        
        lab_printer.tick()
    
    average_wait = sum(waiting_times) / len(waiting_times)
    print(f"Average wait {average_wait} secs {print_queue.size()} tasks remaining.")

for i in range(10):
    simulation(20, 20, 3600, 5)

