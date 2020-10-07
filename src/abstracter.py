"""
Module to fetch abstracted info on each article in the top search results
"""

from Bio import Entrez
from Bio import Medline

def fetch(query_key, webenv, database, results_number):
    """
    Fetches abstracted info from NIH databases for a number of articles with corresponding top search results' ids in (query_key, webenv)
    :param query_key:
    :param webenv:
    :param database:
    :param results_number:
    :return: abstracted info on each search result
    """
    # downloading Medline records in the Medline flat-file format,
    handle = Entrez.efetch(db=database, webenv=webenv, query_key=query_key, retmax=results_number, rettype="medline", retmode="text")
    # handle = Entrez.efetch(db="pubmed", id=idlist, .....)
    # would result in separate search and fetch executions,
    # NIH (NCBI) advises to take advantage of their history support in this situation as follows:
    # userhistory='y' resulted in WebEnv and QueryKey arguments, that we use in fetch instead of using a list of ids

    records = Medline.parse(handle)
    records = list(records)    # converting records to a list
    handle.close()

    return records


