import requests
import json

def update_description(trello_key, trello_token, card_id, new_card_description):
    header = {
        "Content-Type": "application/json",
    }
    payload = {
        "desc": new_card_description
    }
    r = requests.put(
        "https://api.trello.com/1/cards/" + card_id + "?key=" + trello_key + "&token=" + trello_token,
        headers=header,
        data=json.dumps(payload),
    )

def update_checklist_on_label(trello_key, trello_token, card_id, label_text, label_checklist):
    if label_text in label_checklist:
        checklist_id = label_checklist.get(label_text)
        header = {
            "Content-Type": "application/json",
        }
        payload = {
            "name": label_text,
            "idChecklistSource": checklist_id
        }
        r = requests.post(
            "https://api.trello.com/1/cards/" + card_id + "/checklists" + "?key=" + trello_key + "&token=" + trello_token,
            headers=header,
            data=json.dumps(payload),
        )
    else:
        pass
