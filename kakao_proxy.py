from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# 카카오 access token — 서버에 보관
ACCESS_TOKEN = "nVYHsVZR-sJ04iVVNDTnR2H4_d-xbEG5AAAAAQoXC2sAAAGWWROtHhamEcnPBcmr"

@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.json
    text = data.get("text", "기본 메시지입니다.")

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    template = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://www.google.com",
            "mobile_web_url": "https://www.google.com"
        },
        "button_title": "확인하기"
    }

    payload = {
        "template_object": json.dumps(template)
    }

    response = requests.post(url, headers=headers, data=payload)

    return jsonify({
        "status": response.status_code,
        "result": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
