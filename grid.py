# GRID

# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# 2. Write a function that draws a similar grid with four rows and four columns

topLine = "+ "+4*"- "
midLine = "|"+9*" "
topColumn = "+"
endColumn = "|"
endLine = 4*topLine + topColumn


def cell():
    print(4*topLine + topColumn)
    print(4*midLine + endColumn)
    print(4*midLine + endColumn)
    print(4*midLine + endColumn)
    print(4*midLine + endColumn)


def doubleCell():
    cell()
    cell()
    cell()
    cell()
    print(endLine)


doubleCell()
