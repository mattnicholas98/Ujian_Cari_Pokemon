# HANYA CONTOH - BUAT NGE-TEST DOANG

'''
import requests

cariPokemon = input('Pokemon yang mau dicari : ')
url = 'https://pokeapi.co/api/v2/pokemon/'+cariPokemon

dataPokemon = requests.get(url)

print('Nama = ', dataPokemon.json()['name'])
print('ID = ', dataPokemon.json()['id'])
print('Tinggi = ', dataPokemon.json()['height'])
print('Berat = ', dataPokemon.json()['weight'])
'''