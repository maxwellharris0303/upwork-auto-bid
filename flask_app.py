from flask import Flask, request, jsonify
from flask_cors import CORS
import main_upwork_bot
import main_upwork_bot_temp_mail
import base64
from datetime import datetime


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/start-bot', methods=['POST'])
def start_upwork_bot():
    # print("hello")
    data = request.get_json()
    print(data)
    userId = data["userId"]
    campaign = data['campaign']
    searchPhase = data['searchPhase']
    print(searchPhase)
    modifiedSearchPhase = searchPhase.replace(", ", " OR ").replace(" ", "%20")
    print(modifiedSearchPhase)
    create_account_count = data['create_account_count']
    print(create_account_count)
    email, first_name, last_name, photo_path, hourly_rate, bid_amount, job_desc_text, response_chatgpt_array = main_upwork_bot.main(create_account_count, campaign, modifiedSearchPhase)
    print(email, first_name, last_name, photo_path, hourly_rate, bid_amount)

    return "Done"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)