import logging

logging.basicConfig(
    filename="logss.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("This is a log message")


def a():
    print("Start of a()")
    b()


ye = "fe"


def b():
    global ye
    print(ye)
    print("Start of b()")
    return ye


logging.debug(b())


def c():
    print("Start of c()")
    25 / 0


def spam(number1, number2):
    logging.debug(number1)
    return number1 / (number2 - 42)


spam(101, 43)

logging.debug(ye)
