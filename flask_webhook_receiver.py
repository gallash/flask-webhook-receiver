from flask import Flask, request, abort
# from OpenSSL import SSL

app = Flask(__name__)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return "<h1>Welcome to Simple Flask Webhook Receiver!</h1>"

    if request.method == 'POST':
        print(request.get_json(force=True)) # Forces to pass request data as JSON
        return 'success', 200

    else:
        abort(400)

if __name__ == '__main__':
    app.run() 
