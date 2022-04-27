from flask import Flask, request

# https://python-binance.readthedocs.io/en/latest/binance.html?highlight=futures_create_order#binance.client.Client.futures_create_order

app = Flask(__name__)
# bot = MainBot()  # Handles all telegram communication


@app.route('/', methods=['GET'])
def index():
    return {"Status": "OK"}


@app.route('/botwebhook', methods=['POST'])
def webhook_process():
    # client = Binance(config.SPOTTEST_API_KEY, config.SPOTTEST_SECRET_KEY)
    return {"Status": "OK"}
