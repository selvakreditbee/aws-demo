""" Main File """
import os
from dotenv import load_dotenv
import math


load_dotenv()


def sample():
    """
    Sample function
    """
    return "hi"


if __name__ == '__main__':
    print("Read from environment")
    name = os.getenv("MY_NAME")
    print("From Environment: {name}".format(name=name), "dmvlsmv")
    print("Hi Check the pylint")
