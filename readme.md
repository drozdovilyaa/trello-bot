# Trello bot
The app is designed to automate some repetitive manual actions. Firstly, it should add a template description to all newly created cards. Secondly, it should create a new checklist when a label is added to the card. Each label has one associated checklist.

PS: Trello Power-up Butler provide the same functionality and even more features. However, the number of actions is limited in the free version.

## Main functions

1. Add a template description to the newly created card.         
![](https://media.giphy.com/media/Ie9yT1wNkRhD6clsIl/giphy.gif)

2. Add a checklist to the card when the new label is added to it.
![](https://media.giphy.com/media/W08JC36zs9dVg4JTae/giphy.gif)

## Script setup
1. [Visit this page](https://trello.com/app-key) to create Trello API key and token. For more information visit official Trello [documentation](https://developer.atlassian.com/cloud/trello/) page.
2. Add your API key and token to config.py file.
3. Open the board you want to automate.
4. Add `.json` at the end of the URL of your board (Example: `https://trello.com/b/xxxxxxxx/demo-board.json`). Open it in your browser.
5. Copy id of the board to config.py file
```json
{"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "name":"Demo board",
   "desc":"",
   "descData":null,
   "closed":false,
   "idOrganization":null,
   "shortLink":"xxxxxxxx",
   ...
```
6. Create a template card. It will store your checklists. Make sure that this card will not be deleted later. Otherwise, you have to reconfigure the script.
7. Create labels with a descriptive name.
8. Add a new checklist.                                          
![](https://media.giphy.com/media/S9oLgz2t4ZW3BaARjI/giphy.gif)
9. Add .json to the URL of your template card (Example: `https://trello.com/c/xxxxxxxx/9-new-card.json`) and find the id of the new checklist.
```json
    ...
    "checklists":[
          {
             "id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
             "name":"Translate",
             "idCard":"xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
             "pos":16384,
             "creationMethod":null,
             "idBoard":"xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
             "checkItems":[ 
             ...
```
10. Add label name and id of associated checklist to the config.py file.
11. If you need more labels and checklists repeat steps 7-10.
12. Set card description in config.py file.
13. Set a secret key. If someone will try to send requests to your app, this will help to protect your board from an authorized requests.
14. Deploy your app. Find more info on [Heroku](https://devcenter.heroku.com/articles/git "Heroku") or [Youtube](https://www.youtube.com/results?search_query=heroku+deploy+python "Youtube").
15. Register Trello Webhook by sending a POST request. For more information about Trello Webhooks visit [this page](https://developer.atlassian.com/cloud/trello/guides/rest-api/webhooks/)
URL:` https://api.trello.com/1/tokens/add_your_trello_token_here/webhooks/`
Body:
```json
{
  "key": "Your_Trello_Key",
  "callbackURL": "https://your_app_URL",
  "idModel":"Your_board_ID",
  "description": "My first webhook"  
}
```
