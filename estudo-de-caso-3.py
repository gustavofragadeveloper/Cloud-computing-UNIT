
import requests
import random

API_KEY = "B1UHZ6SK3OJAADC9"

BASE_URL = f"https://api.thingspeak.com/update"

valor = input('Digite um valor: ')
print(f"O valor enviado foi; {valor}")

payload = {
    "api_key": API_KEY,
    "field1": valor
}

response = requests.post(BASE_URL, params=payload)

if response.status_code == 200:
  print("Dados enviados com sucesso para o Thingspeak!")
else:
  print("Erro ao enviar dados para o Thingspeak")