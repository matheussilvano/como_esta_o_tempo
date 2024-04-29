import requests
import os
from time import sleep

api_key = '077df67e14f09d23a802f193d0d1c9c0'

print('Feito por Matheus Silvano')
sleep(1)
os.system('clear')

while True:
    print('Como está o clima?')
    cidade = input('Digite o nome da cidade desejada: ').capitalize()
    os.system('clear')
    tempo = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br'
    requisicao = requests.get(tempo)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura_kelvin = requisicao_dic['main']['temp']
    temperatura_celsius = temperatura_kelvin - 273.15
    pais = requisicao_dic['sys']['country']
    vento_mpors = requisicao_dic['wind']['speed']
    vento_kmporh = vento_mpors * 3.6
    print(f'Em {cidade}-{pais}, a temperatura atual é de {temperatura_celsius:.1f}°C, com {descricao} e ventos de até {vento_kmporh:.1f}Km/h')
    sleep(1)
    input('Digite enter para esolher outra cidade: ')
    os.system('clear')
