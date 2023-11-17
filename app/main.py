from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

translator = GoogleTranslator(source="pt", target="en")

@app.route("/", methods=['GET', 'POST'])
def index():
    texto = None
    resultado = None

    if request.method == 'POST':
        texto = request.form['text']
        traducao = translator.translate(texto)
        resultado = traducao

    return render_template('index.html', resultado=resultado, texto=texto)

if __name__ == "__main__":
    app.run(debug=False)
