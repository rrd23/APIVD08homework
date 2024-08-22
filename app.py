from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Запрос к API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random')
    quote_data = response.json()

    # Извлечение текста цитаты и автора
    quote = quote_data['content']
    author = quote_data['author']

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
