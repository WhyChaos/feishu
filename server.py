#!/usr/bin/env python3.8

import logging
import os

import requests
from api import MessageApiClient
from dotenv import find_dotenv, load_dotenv
from event import EventManager, MessageReceiveEvent, UrlVerificationEvent
from flask import Flask, jsonify

# load env parameters form file named .env
load_dotenv(find_dotenv())

app = Flask(__name__)

# load from env
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ENCRYPT_KEY = os.getenv("ENCRYPT_KEY")
LARK_HOST = os.getenv("LARK_HOST")

# init service
message_api_client = MessageApiClient(APP_ID, APP_SECRET, LARK_HOST)
event_manager = EventManager()


@event_manager.register("url_verification")
def request_url_verify_handler(req_data: UrlVerificationEvent):
    # url verification, just need return challenge
    if req_data.event.token != VERIFICATION_TOKEN:
        raise Exception("VERIFICATION_TOKEN is invalid")
    return jsonify({"challenge": req_data.event.challenge})


@event_manager.register("im.message.receive_v1")
def message_receive_event_handler(req_data: MessageReceiveEvent):
    print("---------message_receive_event_handler")
    sender_id = req_data.event.sender.sender_id
    message = req_data.event.message
    if message.message_type != "text":
        logging.warn("Other types of messages have not been processed yet")
        return jsonify()
        # get open_id and text_content
    open_id = sender_id.open_id
    text_content = message.content
    # echo text message
    print(type(text_content))
    print(text_content)
    print(eval(text_content)["text"])
    message_api_client.send_text_with_open_id(open_id, text_content)
    return jsonify()


@event_manager.register("p2p_chat_create")
def p2p_receive_event_handler(req_data: MessageReceiveEvent):
    sender_id = req_data.event.sender.sender_id

    print(sender_id)
    print("监听到首次会话被创建")
    return jsonify()


@event_manager.register("card.action.trigger")
def card_receive_event_handler(req_data: MessageReceiveEvent):
    # sender_id = req_data.event.sender.sender_id

    print(req_data.event.action)
    print("卡片回传")
    return jsonify()


@app.errorhandler
def msg_error_handler(ex):
    logging.error(ex)
    response = jsonify(message=str(ex))
    response.status_code = (
        ex.response.status_code if isinstance(ex, requests.HTTPError) else 500
    )
    return response


@app.route("/", methods=["POST"])
def callback_event_handler():
    # init callback instance and handle
    print("-----------callback_event_handler")
    event_handler, event = event_manager.get_handler_with_event(
        VERIFICATION_TOKEN, ENCRYPT_KEY
    )
    return event_handler(event)


if __name__ == "__main__":
    # init()
    app.run(host="0.0.0.0", port=8080, debug=True)
