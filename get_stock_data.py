#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import os

base_url = "http://ichart.finance.yahoo.com/table.csv?s="


def touch(path):
    with open(path, 'w'):
        os.utime(path, None)


def make_url(ticker_symbol):
    return base_url + ticker_symbol


output_path = "."


def make_filename(ticker_symbol, directory="stock_data"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"


def pull_historical_data(ticker_symbol, directory="stock_data"):

    outfilename = output_path + \
        "/" + "stock_data/" + ticker_symbol + ".csv"
    touch(outfilename)

    try:
        urllib.urlretrieve(
                make_url(ticker_symbol),
                make_filename(ticker_symbol, directory))

    except urllib.ContentTooShortError as e:
        outfile = open(outfilename, "w")
        outfile.write(e.content)
        outfile.close()


if __name__ == "__main__":
    tickers = [
            "WMT",
            "FB",
            "SBUX",
            "UAL",
            "NKE",
            "XOM",
            "ADR",
            "USO",
            "UNG",
            "JO",
            "SOYB",
            "BAL"]
    for t in tickers:
        print "Getting data for " + t
        pull_historical_data(t)
