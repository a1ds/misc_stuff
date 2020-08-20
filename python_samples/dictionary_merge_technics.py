"""Dictionaries merging techniques"""


# Inspired by:
# https://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/


# Assuming we have two groups of fruits, and we
# need to merge them. One important notice, we
# have the same fruit (banana) in both groups.
# So keys of dict are names of fruits and values
# are countries (producers).

group_one = {
    "apple": "Poland",
    "peach": "Italy",
    "banana": "Ecuador"
    }

group_two = {
    "ananas": "Brazil",
    "orange": "Mexico",
    "banana": "Thailand"
    }


# -----------------------
# 01 Dictionary unpacking
#
# for Python 3.5 and above (see PEP 448)
# the syntax is
combined_one = {**group_one, **group_two}

# but, you should to remember the order of
# dictionaries is significant in the case. This
# statement will provide you with different
# results comparing to above one.
combined_two = {**group_two, **group_one}
"""result: {'ananas': 'Brazil', 'apple': 'Poland',
'banana': 'Ecuador', 'orange': 'Mexico',
'peach': 'Italy'}"""

# It's important to notice that the country for
# "banana" will be taken from last dictionary in
# the list


# ---------------------------
# 02 Dictionary from ChainMap
#
# for Python 3.3 and above we can use
# collections.ChainMap
from collections import ChainMap

# In this case, order is significant and value
# for 'banana' will be taken from the fist
# dictionary in the list, see ChainMap docs for
# details (https://docs.python.org)
combined = dict(ChainMap(group_one, group_two))
"""result: {'ananas': 'Brazil', 'apple': 'Poland',
'banana': 'Ecuador', 'orange': 'Mexico',
'peach': 'Italy'}"""


# ----------------
# 03 Chained items
# 
from itertools import chain

# This will work for Python 2.7 and above, but if
# you use Python 2.7 it's optimal to use
# iteritems() instead of item() method. Also
# notice, in Python 3 there is no iteritems()
# method of dictionary.
# In this case, value for 'banana' will be taken
# from the last dictionary.
# See `itertools.chain` docs for more
# details (https://docs.python.org)
combined = dict(
    chain(group_one.items(), group_two.items())
    )


# --------------------
# 04 Concatenate items
#
# In these cases, value for 'banana' will be taken
# from the last dictionary.

# for Python 3
combined = dict(
    (list(group_one.items()) +
     list(group_two.items()))
     )

# for Python 2
# combined = dict(
#    group_one.items() + group_two.items()
#    )


# ------------------
# 05 Copy and update
#
# For Python 2.7 and above, order is significant
combined = group_one.copy()
combined.update(group_two)
