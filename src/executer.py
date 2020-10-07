"""
Module to execute the search query to get and output the top search results
"""

from writer import printout
from searcher import search
from abstracter import fetch

def execute(query, database, results_number):
    """
    Executes query and outputs a number of the top search results
    :param query:
    :param database:
    :param results_number:
    :return:
    """
    (query_key, webenv) = search(query, database, results_number)

    records = fetch(query_key, webenv, database, results_number)

    printout(records)

    return





