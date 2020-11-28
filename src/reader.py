"""
Module to read the query and other inputs
"""

from Bio import Entrez
from filter import filter_selector

def inputnow():
    """
    Reads the inputs' values
    :return: query
    """
    # the email must be the user's individual/personal email (NOT an institutional email or a default email
    # as this could lead to exceeding the maximum allowable frequency of requests per user, of 3 per second)
    Entrez.email = "davidrivas@blockchainguru.ca"

    # The maximum number of search results to be displayed could be the following default value or an input value < 100
    results_number = 5

    query = input("enter your search query: ")

    filter_option = input("would you like to use advanced search filter? (yes/no): ")
    if (filter_option == "yes"):
        query = filter_selector(query)

    return query, results_number
