### REST API for Multiplayer Chess Game with Flask & MongoDB
*under development. websocket configs for realtime data are catching up*
# Prerequisite
1. Python >= 3.9.1
2. pip >= 20.2.3
3. MongoDB >= 4.4


# Usage
1. run> `python -m venv env`
2. run> `.\env\Scripts\activate`
3. run> `pip install -r requirements.txt`
4. fill .example.env with your own configs, and rename it to .env
5. run> `flask run` (flask will run depends on config at .flaskenv) `by default, your app will run on port 5000`


# Available Services
- [x] **User:** /api/v1/user
- [x] **Auth:** /api/v1/auth
- [x] **Auth:** /api/v1/game
