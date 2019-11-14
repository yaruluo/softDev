# Justin & Yaru
# SoftDev1 pd01
# K#25 -- Getting More REST
# 2019-11-13

from flask import Flask, render_template
from flask import request
import urllib, json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/restcountries")
def country_api_request():
    url = "https://restcountries.eu/rest/v2/alpha/tv"
    request = urllib.request.urlopen(url).read()
    print(request)
    parsed = json.loads(request)
    print(parsed)
    return render_template("country.html", to_render=parsed, title="restcountries API")

@app.route("/metcollection")
def met_api_request():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/47389"
    request = urllib.request.urlopen(url).read()
    print(request)
    parsed = json.loads(request)
    print(parsed)
    return render_template("met.html", to_render=parsed, title="Met collection API")

@app.route("/exchangerate")
def currency_api_request():
    url = "https://api.exchangerate-api.com/v4/latest/AUD"
    request = urllib.request.urlopen(url).read()
    print(request)
    parsed = json.loads(request)
    print(parsed)
    return render_template("currency.html", to_render=parsed, title="Exchange rate API")

@app.route("/rickandmorty")
def randm_api_request():
    url = "https://rickandmortyapi.com/api/episode/31"
    request = urllib.request.urlopen(url).read()
    print(request)
    parsed = json.loads(request)
    print(parsed)
    return render_template("randm.html", to_render=parsed, title="Rick and Morty API")

@app.route( '/IPaddress')
def ip_location_request():
    url = 'http://ip-api.com/json/64.09.1.2'
    request = urllib.request.urlopen( url).read()
    print( request)
    parsed = json.loads( request)
    print( parsed)
    return render_template( 'ip.html', to_render = parsed, title = "IP API")

@app.route( '/superhero')
def _request():
    url = 'http://superheroapi.com/api.php/2503373653110667/720'
    request = urllib.request.urlopen( url).read()
    print( request)
    parsed = json.loads( request)
    print( parsed)
    return render_template( 'hero.html', to_render = parsed, title = "Hero API")

if __name__ == "__main__":
    app.debug = True
    app.run()
