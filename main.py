import json
import requests
import hashlib


class Search_countries:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, encoding='utf-8') as f:
            json_data = json.load(f)
            self.country_list = [country["name"]["common"] for country in json_data]
            self.quantity_country = len(self.country_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.quantity_country -= 1
        if self.quantity_country == -1:
            raise StopIteration
        url = 'https://en.wikipedia.org/wiki/' + '_'.join(self.country_list[self.quantity_country].split(' '))
        r = requests.head(url)
        if r.status_code == 200:
            return f'{self.country_list[self.quantity_country]} - {url}'
        else:
            print(f'{self.country_list[self.quantity_country]} - Ошибка')


if __name__ == '__main__':
    with open('final.txt', 'w', encoding='utf-8') as ouf:
        for i in Search_countries("countries.json"):
            ouf.write(i + '\n')



def hash_countries(file_path):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            hash_object = hashlib.md5(line.strip().encode())
            yield hash_object.hexdigest()



if __name__ == '__main__':
    for i in hash_countries('final.txt'):
        print(i)