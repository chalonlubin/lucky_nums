from random import randint
import requests

NUMBERS_API_URL = "http://numbersapi.com/"

def get_num_fact(num):
    """Request fact from Numbers API based on any number."""
    return requests.get(
            f"{NUMBERS_API_URL}{num}").text

def get_year_fact(year):
    """Request fact from Numbers API based a year."""
    return requests.get(
            f"{NUMBERS_API_URL}{year}/year").text

def random_number(small, large):
    """Return a random number between 1-100 (inclusive)
    >>> random_number(1,1)
    1
    """
    return randint(small, large)

def serialize_random_facts(num, year):
    """Create a response of random facts from numbers API from
    (num) and (year) input that can be easily converted into JSON.
    """
    response = {
        "num": {
            "fact": get_num_fact(num),
            "num": num
        },
        "year": {
            "fact": get_year_fact(year),
            "year": year
        }
    }
    return response