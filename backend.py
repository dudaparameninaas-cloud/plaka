from flask import Flask, request, Response
import json

app = Flask(__name__)

with open("plakalar.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

def normalize(text):
    return text.upper().strip()

@app.route("/")
def home():
    return Response(json.dumps({"status": "ok", "message": "Plaka API aktif"}, ensure_ascii=False),
                    mimetype="application/json")

@app.route("/plaka")
def plaka_sorgu():
    plaka = request.args.get("plaka")
    if not plaka:
        return Response(json.dumps({"error": "plaka parametresi eksik"}, ensure_ascii=False),
                        mimetype="application/json")

    plaka = normalize(plaka)
    sonuc = [x for x in DATA if normalize(x["plaka"]) == plaka]

    return Response(json.dumps(sonuc, ensure_ascii=False), mimetype="application/json")

@app.route("/plaka-ad")
def ad_sorgu():
    ad = request.args.get("ad")
    if not ad:
        return Response(json.dumps({"error": "ad parametresi eksik"}, ensure_ascii=False),
                        mimetype="application/json")

    ad = normalize(ad)
    sonuc = [x for x in DATA if ad in normalize(x["isim"])]

    return Response(json.dumps(sonuc, ensure_ascii=False), mimetype="application/json")

@app.route("/plaka-soyad")
def soyad_sorgu():
    soyad = request.args.get("soyad")
    if not soyad:
        return Response(json.dumps({"error": "soyad parametresi eksik"}, ensure_ascii=False),
                        mimetype="application/json")

    soyad = normalize(soyad)
    sonuc = [x for x in DATA if soyad in normalize(x["isim"])]

    return Response(json.dumps(sonuc, ensure_ascii=False), mimetype="application/json")

@app.route("/plaka-adsoyad")
def adsoyad_sorgu():
    ad = request.args.get("ad")
    soyad = request.args.get("soyad")

    if not ad or not soyad:
        return Response(json.dumps({"error": "ad ve soyad gerekli"}, ensure_ascii=False),
                        mimetype="application/json")

    ad = normalize(ad)
    soyad = normalize(soyad)

    sonuc = [
        x for x in DATA
        if ad in normalize(x["isim"]) and soyad in normalize(x["isim"])
    ]

    return Response(json.dumps(sonuc, ensure_ascii=False), mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
