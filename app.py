import requests
import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

api_pepet = os.getenv("WEATHER_API_KEY")

@app.route('/api/suggestions')
def suggestions():
    query = request.args.get('q', '')
    res = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_pepet}')
    return jsonify(res.json())



@app.route("/", methods=["GET", "POST"])
def home():
    data_cuaca = None

    if request.method == "POST":
        kota = request.form["kota"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_pepet}&units=metric"
        respon = requests.get(url)
        data = respon.json()

        if data["cod"] == 200:
            data_cuaca = {
                "kota": kota,
                "temp": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            data_cuaca = {"error": "Kota tidak ditemukan"}

    return render_template("index.html", cuaca=data_cuaca)

if __name__ == "__main__":
    app.run(debug=False)