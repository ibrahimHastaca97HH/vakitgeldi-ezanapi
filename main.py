from flask import Flask, jsonify
from datetime import datetime
from hijri_converter import convert

app = Flask(__name__)

@app.route('/api/v1/vakitler')
def get_prayer_times():
    il = "Hatay"
    ilce = "Yayladağı"
    konum = f"{ilce}, {il}"

    miladi_tarih = datetime.now()
    miladi_str = miladi_tarih.strftime("%d %b %Y")

    hijri_tarih = convert.Gregorian(miladi_tarih.year, miladi_tarih.month, miladi_tarih.day).to_hijri()
    hicri_str = f"{hijri_tarih.day} {hijri_tarih.month_name()} {hijri_tarih.year}"

    vakitler = {
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

    response = {
        "konum": konum,
        "il": il,
        "ilce": ilce,
        "tarih": miladi_str,
        "hicri_tarih": hicri_str,
        "vakitler": vakitler
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
