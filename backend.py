from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Lokal JSON yükle (Render için ideal)
with open("plakalar.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

def normalize(text):
    return text.upper().strip()

@app.route("/")
def home():
    return {"status": "ok", "message": "Plaka API aktif"}

# 1️⃣ Plaka ile sorgu
@app.route("/plaka")
def plaka_sorgu():
    plaka = request.args.get("plaka")
    if not plaka:
        return {"error": "plaka parametresi eksik"}

    plaka = normalize(plaka)
    sonuc = [x for x in DATA if normalize(x["plaka"]) == plaka]

    return jsonify(sonuc)

# 2️⃣ Ada göre sorgu
@app.route("/plaka-ad")
def ad_sorgu():
    ad = request.args.get("ad")
    if not ad:
        return {"error": "ad parametresi eksik"}

    ad = normalize(ad)
    sonuc = [x for x in DATA if ad in normalize(x["isim"])]

    return jsonify(sonuc)

# 3️⃣ Soyada göre sorgu
@app.route("/plaka-soyad")
def soyad_sorgu():
    soyad = request.args.get("soyad")
    if not soyad:
        return {"error": "soyad parametresi eksik"}

    soyad = normalize(soyad)
    sonuc = [x for x in DATA if soyad in normalize(x["isim"])]

    return jsonify(sonuc)

# 4️⃣ Ad + Soyad
@app.route("/plaka-adsoyad")
def adsoyad_sorgu():
    ad = request.args.get("ad")
    soyad = request.args.get("soyad")

    if not ad or not soyad:
        return {"error": "ad ve soyad gerekli"}

    ad = normalize(ad)
    soyad = normalize(soyad)

    sonuc = [
        x for x in DATA
        if ad in normalize(x["isim"]) and soyad in normalize(x["isim"])
    ]

    return jsonify(sonuc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
