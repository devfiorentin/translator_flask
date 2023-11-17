from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="pt", target="en")

texto = input("Digite: ")

traducao = translator.translate(texto)
print(translator.translate(texto))
