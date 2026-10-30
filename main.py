# LGN BOT - by digi03
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>🔥 LGN BOT AKTIF BOS! 🔥</h1>
    <p>Bot LGN berhasil jalan di PythonAnywhere</p>
    <p>Waktu: {datetime.datetime.now()}</p>
    <p>Status: ONLINE ✅</p>
    <hr>
    <p>Repo: digi03/LGN</p>
    """

@app.route('/bot')
def bot_status():
    return {"status": "online", "bot": "LGN", "owner": "digi03"}

if __name__ == '__main__':
    app.run()

# Fungsi tambahan LGN
def lgn_logic(pesan):
    # disini nanti logic bot Telegram / Discord bos
    if "halo" in pesan.lower():
        return "Halo bos! LGN siap!"
    return f"LGN terima: {pesan}"
