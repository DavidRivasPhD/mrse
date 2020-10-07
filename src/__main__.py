"""
Main sequence to input the query and obtain corresponding search results
"""

from reader import inputnow
from executer import execute

# query input
(query, results_number) = inputnow()

# obtaining top results for articles' ABSTRACTS
database = "pubmed"
execute(query, database, results_number)

# obtaining top results for articles' FULL TEXTS
database = "pmc"
execute(query, database, results_number)

print("If you are not satisfied with the search results, try shorter/longer/equivalent queries with/without a filter. Thank you.")
