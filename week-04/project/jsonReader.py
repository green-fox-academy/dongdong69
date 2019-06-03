import json

class jsonReader():

    def __init__(self, file_url):
        with open(file_url, 'r') as jsonr:
            self.string_record = jsonr.read()
            self.records_dict = json.loads(self.string_record)
            
    def get_records(self):
        return self.records_dict

    def get_string(self):
        return self.string_record