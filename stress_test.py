from multiprocessing import Pool

import requests


def make_request(x):
    response = requests.get('http://localhost:8000/test2')
    print(response.status_code)
    return response.status_code


if __name__ == '__main__':
    p = Pool(10)
    for i in range(20):
        p.map(make_request, range(10))
