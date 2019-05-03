from flask import Flask, render_template, request, redirect, url_for, abort
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

# POST route
@app.route('/post', methods = ['POST'])
def postCari():
    nam = request.form['nama']

    return redirect(url_for('hasilPokemon', nama = nam))
    
# route buat hasilnya
@app.route('/hasil/<string:nama>')
def hasilPokemon(nama):

    cariPokemon = nama.lower()

    url = 'https://pokeapi.co/api/v2/pokemon/'+cariPokemon
    dataPokemon = requests.get(url)

    if str(dataPokemon) == '<Response [404]>':
        abort(404)
    else:
        return render_template('showpage.html', dataPokemon = dataPokemon)


# 404 route
@app.errorhandler(404)
def error404(error):
    return render_template('errorpage.html')


if __name__ == '__main__':
    app.run(debug = True)