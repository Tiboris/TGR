#!/usr/python3
from graphs import Network
from nodes import Transformer


def transformers_status_ok(transformers):
    return not transformers.has_loop()


def run(data):
    transformers = Network(data, Transformer, " - ", ": ")

    if transformers_status_ok(transformers):
        print("Stav site OK")
    else:
        print("Stav site ERROR")
