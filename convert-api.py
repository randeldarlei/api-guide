import requests
import json

#Request to API 
cotacoes = requests.get("https://economia.awsomeapi.com.br/last/USD-BRL,EUR-BRL, BTC-BRL")

#Send output json to variable
cotacoes = cotacoes.json()

#Get Dollar quote with bid param
cotacoes = cotacoes['USDBRL']["bid"]

#Print output 
print(cotacoes)

