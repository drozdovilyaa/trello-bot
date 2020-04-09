from flask import Flask, request
from config import *
from card_update_functions import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'HEAD'])
def webhook():
    # Return 200 to register webhook
    if request.method == 'HEAD':
        return '{\"Status\":\"Ok\"}', 200

    if request.method == 'POST':
        # Check token to proceed
        if request.args.get('verify_token') == secret_key:
            req_data = request.get_json()
            # New card added
            if req_data['model']['id'] == board_id and req_data['action']['type'] == "createCard":
                card_id = req_data['action']['data']['card']['id']
                update_description(trello_key, trello_token, card_id, new_card_description)
                return '{\"Status\":\"Card comment updated\"}', 200
            # New label added to card
            if req_data['model']['id'] == board_id and req_data['action']['type'] == "addLabelToCard":
                card_id = req_data['action']['data']['card']['id']
                label_text = req_data['action']['data']['label']['name']
                update_checklist_on_label(trello_key, trello_token, card_id, label_text, label_checklist)
                return '{\"Status\":\"Card checklist updated\"}', 200
            # No registered actions
            else:
                return '{\"Status\":\"No recognised action\"}', 200
        # Wrong token
        else:
            return '{\"Status\":\"Bad token\"}', 401
    # Other request methods
    else:
        return '{\"Status\":\"Method not allowed\"}', 405

if __name__ == '__main__':
    app.run()
