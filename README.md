# Flask Webhook Receiver
This Python project uses Flask as the Web Framework to build the webhook receiver.

The Webhook Receiver will receive the JSON message and display it in the terminal.

The implementation is straightforward and uses no method of idempotency or authentification. These features are intended to be implemented in future updates.

## Getting started
After cloning the repo to the local machine, create and activate a virtual environment by running:

```bash
virtualenv -p <PATH_TO_PYTHON3.X, e.g., /urs/bin/python3.8> <name of the virtual environment, e.g., venv>
 
source venv/bin/activate
```

Install the dependencies

```bash
pip3 install -r requirements.txt
``` 

Change the necessary settings in the `flask_webhook_receiver.py` file.

Can also run SSL by uncommenting the `OpenSSL` import, at the top of the file, and passing the ssl\_certificate argument in the `app.run` function call.

It is also possible to run on `host=0.0.0.0`, `port=5000` instead of localhost (set by default) by making it explicit in the `app.run` function call.

## Running the Webhook Receiver

Simply run, in the terminal, the command:

```bash
python3 flask_webhook_receiver.py
```
