import json
from tqdm import tqdm
import time


class DataReader(object):
    data: list

    def __init__(self, path: str):
        self.data = json.load(open(path, encoding='1251'))


if __name__ == '__main__':
    reader = DataReader('82.txt')
    with tqdm(total=len(reader.data)) as progressbar:
        for item in reader.data:
            progressbar.update(5)
