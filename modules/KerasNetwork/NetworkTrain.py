# This program is intended to produce a Keras Model
# trained to predict whether or not a stock is positioned
# to increase of decrease in value. With that determination,
# it will decided whether or not to buy, sell, or pass on a 
# certain stock.
#
# Sam Gulinello 2021

from resources.indices import index
from resources.Stock.stock import Stock
from resources.TD.td import TD
from config.config import config
from main import stockDict


def main():
    indices = index["S&P"]

    