
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

def CheckLogin(id, remote):
    b64_decode_result = "".join([chr(i) for i in list(base64.standard_b64decode(id))])
    encoded_str_for_hashing = b64_decode_result.encode('utf-8')
    #print(encoded_str_for_hashing)
    sha256_result = hashlib.sha256(encoded_str_for_hashing).hexdigest()
    #print(sha256_result ,sha256_result == remote)
    return (b64_decode_result, sha256_result == remote)

def decodeId(id):
    prepared_id = id.encode('utf-8') 
    b64_decode_result = "".join([chr(i) for i in list(base64.standard_b64decode(prepared_id))])
    return b64_decode_result
#print(CheckLogin("dXNlcg==", "04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb"))
#print(decodeId("dXNlcg=="))