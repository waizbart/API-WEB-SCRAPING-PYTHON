from urllib.request import urlopen
from bs4 import BeautifulSoup

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = "bitcoin"


app = Flask(__name__)
api = Api(app)


class dolar(Resource):
    def get(self):
        url = []
        for site in search(query, tld="co.in", num=1, stop=1, pause=1):
            url.append(site)
        html = urlopen(url[0])
        bs = BeautifulSoup(html, 'html.parser')
        input = bs.find_all('input', {'id': 'nacional'})
        dolar = float(input[0].get("children").replace(",", "."))
        return {"dolar": dolar}


api.add_resource(dolar, '/dolar')

if __name__ == '__main__':
    app.run()
