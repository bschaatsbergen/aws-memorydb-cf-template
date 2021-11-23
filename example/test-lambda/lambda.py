#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
import redis
import names
import random

logger = logging.getLogger()
logger.setLevel(level=os.getenv("LOG_LEVEL", "INFO"))


class Person:
    def __init__(self, person_id, first_name):
        self.person_id = person_id
        self.first_name = first_name


def lambda_handler(event, context):
    r = redis.Redis(host='localhost', port=6379, db=0)

    logger.info("Inserting 5.000 random people")

    people = []

    for item in range(5000):
        rand_name = names.get_first_name()
        rand_int = random.randint()
        people.append(Person(item[rand_int], item[rand_name]))
        r.set(rand_int, rand_name)

    for person in people:
        r.get(person.person_id)


if __name__ == "__main__":
    lambda_handler(None, None)
