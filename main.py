import json
import threading
import requests


def write_to_json_file(products_list):
    json_object = json.dumps(products_list, indent=4)
    with open('products.json', 'w') as products_json:
        products_json.write(json_object)


def fetch_product(products_list, index):
    r = requests.get(f'https://dummyjson.com/products/{index}')

    if r.status_code == 200:
        products_list.append(r.json())
    else:
        print('ERROR: Incorrect status code!')


def run_threads(thread_pool):
    for i in range(0, 100):
        thread_pool.append(threading.Thread(target=fetch_product, args=(products, i+1)))
        thread_pool[i].start()

    for i in range(0, 100):
        thread_pool[i].join()


if __name__ == '__main__':
    threads = []
    products = []

    run_threads(threads)
    write_to_json_file(products)
