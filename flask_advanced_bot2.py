from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import main_upwork_advanced_bot
import base64
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = client["sky_bidder"]
collection = db["upworks"]


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
    sleep_time = data['sleep_time']
    email, first_name, last_name, photo_path, hourly_rate, bid_amount, job_desc_text, response_chatgpt_array = main_upwork_advanced_bot.main(create_account_count, campaign, modifiedSearchPhase, sleep_time)
    print(email, first_name, last_name, photo_path, hourly_rate, bid_amount)

    with open(photo_path, 'rb') as image_file:
        image_data = image_file.read()

    base64_data = base64.b64encode(image_data).decode('utf-8')

    current_datetime = datetime.now()

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    document = {
        "userId": userId,
        "account": {
            "name": first_name + " " + last_name,
            "email": email,
            "avatar": None,
            "password": "1234qwer!@#$"
        },
        "campaign": {
            "title": campaign,
            "hourly_rate": hourly_rate
        },
        "bid": {
            "search_filter": searchPhase,
            "job_description": job_desc_text,
            "cover_letter": response_chatgpt_array,
            "bid_amount": bid_amount
        },
        "created_time": formatted_datetime
    }
    collection.insert_one(document)
    query = {"userId": userId}
    documents = collection.find(query)
    if len(list(documents)) != 0:
        print("Success")
        document['_id'] = str(document['_id'])
        return document
    else:
        print("Error")
        return "Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82)