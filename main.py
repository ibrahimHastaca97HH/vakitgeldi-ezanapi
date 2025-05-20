from flask import Flask, jsonify
from datetime import datetime
from hijri_converter import convert

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Vakitgeldi Ezan API çalışıyor."})

@app.route("/vakitler")
def get_vakitler():
    # Tarih bilgisi
    miladi_tarih = datetime.today()
    hicri_tarih = convert.Gregorian(miladi_tarih.year, miladi_tarih.month, miladi_tarih.day).to_hijri()

    return jsonify({
        "konum": "Hatay, Yayladağı, Turkey",
        "tarih": miladi_tarih.strftime("%d %B %Y"),
        "hicri": f"{hicri_tarih.day} {hicri_tarih.month_name()} {hicri_tarih.year}",
        "vakitler": {
            "Fajr": "03:33",
            "Sunrise": "05:17",
            "Dhuhr": "12:44",
            "Asr": "17:47",
            "Sunset": "20:00",
            "Maghrib": "20:00",
            "Isha": "21:37",
            "Imsak": "03:23",
            "Midnight": "00:39",
            "Firstthird": "23:04",
            "Lastthird": "02:14"
        }
    })
