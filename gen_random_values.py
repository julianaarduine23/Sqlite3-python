import random
import rstr
import datetime

def gen_age():
    return random.randint(15,99) #gera idade
def gen_cpf():
    return rstr.rstr('1234567890', 11) #gera cpf
def ge_phone():
    return '({0}) {1}-{2}'.format(  #gera telefone
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4))
def gen_timestamp():    #gera data e hora
    year = random.randint(1980, 2015)
    month = random.randint(1, 12)
    day = random.randint(1,28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(year, month, day, hour, minute, second,microsecond).isoformat(" ")
    return date
def gen_city():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'RIO DE JANEIRO', 'RJ'],
        [u'PORTO ALEGRE', 'RS'],
        [u'CAMPO GRANDE', 'MS']]
    return random.choice(list_city)
