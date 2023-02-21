#!/usr/bin/env python3
'''Page index range'''
import csv
import math
from typing import Dict, List, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Tuple containing a start and end index'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Dataset pages'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List, None]]:
        '''Context page'''
        page_content = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_data = {
            'page_size': len(page_content),
            'page': page,
            'data': page_content,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_page': total_pages
        }
        return page_data
