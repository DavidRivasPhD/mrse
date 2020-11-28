"""
Module to use the search engine
"""

from Bio import Entrez

def search(query, database, results_number):
    """
    Searches a NIH database by using a NIH's relevance/best-match/AI algorithm through Bio-Entrez
    :param query:
    :param database:
    :param results_number:
    :return: articles ids of top search results (stored and identified in NIH's server through query_key & webenv)
    """
    handle = Entrez.esearch(db=database, retmax=results_number, term=query, usehistory='y', sort='relevance')

    record = Entrez.read(handle)

    query_key = record["QueryKey"]
    webenv = record["WebEnv"]

    return query_key, webenv
