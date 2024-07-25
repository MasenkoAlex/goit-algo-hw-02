import queue
import random
import threading

request_queue = queue.Queue()

# Функція для генерації нової заявки
def generate_request():
    request_id = random.randint(1, 1000)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги")

# Функція для обробки заявки
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється")
    else:
        print("Черга порожня")


generate_thread = threading.Thread(target=generate_request)
generate_thread.start()
process_request()