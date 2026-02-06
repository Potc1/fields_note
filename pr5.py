
import hashlib
import base64


KEYWORD = 'grac'

class Field():
    def __init__(self, area, name):
        self.area = area
        self.name = name
    def addProcessing(self,  Processing):
        self.arr_processing.add(Processing)
    def get_processing(self):
        return self.arr_processing
    def countPriceProcessing(self, index):
        return self.arr_processing[index].cost_by_once_area * self.area
    
class Processing():
    def __init__(self, name):
        self.name = name
    def setHerbicide(self, herbicide, norma, cost_by_once): 
        self.herbicide = herbicide
        self.norm_herbicide_of_once_are = norma
        self.cost_by_once_herb = cost_by_once 
    def setComment(self,  value):
        self.comment = value
    def getComment(self):
        return self.comment 
    def setField(self, value):
        self.field = value
    def setSeason(self, value):
        self.season = value

def HashLogin(user):
    # слово для кодирования
    word_for_code = f"{user}"
    # Добавляем к ней айди пользователя
    str_for_hash = f"{user}.{KEYWORD}"
    # Переводим в байты
    message = str_for_hash.encode('utf-8')
    # создаём хеш с помощью алгоритма MD5
    md5_hash = hashlib.md5(message).hexdigest()
    print("Ориг: ", str_for_hash, "\nHash: ", md5_hash)
    # кодировка base64
    base64_code = base64.b64encode(word_for_code.encode())
    res_base64_code = "".join([chr(i) for i in list(base64_code)])
    print(f'base64: {res_base64_code}')
    return (md5_hash, res_base64_code)
