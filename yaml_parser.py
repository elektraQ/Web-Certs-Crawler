from libraries import *

class yaml_parser:

    def __init__(self, url_store_obj):
        self.url_store_obj = url_store_obj

    # Read yaml "url_store_obj" returns a list
    def readYAML(self):
        with open('url_store.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data[self.url_store_obj]
