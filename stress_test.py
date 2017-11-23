from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue

import requests


def make_request(num, q):
    print('start thread {}'.format(num))
    while not q.empty():
        index = q.get()
        response = requests.get('http://localhost:8000/test2')
        print('Task {} status_code {}'.format(index, response.status_code))
    print('exit thread {}'.format(num))


if __name__ == '__main__':
    q = Queue()
    for i in range(100):
        q.put(i)

    with ThreadPoolExecutor(10) as executor:
        for i in range(10):
            executor.submit(make_request, i, q)
