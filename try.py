from libraries.tabulate import tabulate
#I moved the directory librares, correct.!

chart1 = {
    "week":"Alcolirykoz"
}
chart2 = {
    "month":"Akapellah"
}

chart3 = {
    "year":"Luis7Lunes"
}

votes_history = [chart1,chart2,chart3]


print(tabulate(votes_history, headers="keys", tablefmt="grid"))

# This is not the best way to reach to the solution, so, we have to re-stablish how handle the charts votes.

#I think, in one list, each user will have 3 places to save their votes. 
# First blank: week
# second blank: month
# third blank: year

new_votes_history = [["Week","Alcolirykoz"],["Month","Akapellah"],["Year","Luis7Lunes"]]

print(tabulate(new_votes_history))

# These are the results:

# First way:
# +-------------+-----------+------------+
# | week        | month     | year       |
# +=============+===========+============+
# | Alcolirykoz |           |            |
# +-------------+-----------+------------+
# |             | Akapellah |            |
# +-------------+-----------+------------+
# |             |           | Luis7Lunes |
# +-------------+-----------+------------+

# Second way:
# -----  -----------
# Week   Alcolirykoz
# Month  Akapellah
# Year   Luis7Lunes
# -----  -----------