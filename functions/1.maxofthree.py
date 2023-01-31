#1
def max_num(a,b,c):
#ternary operator to find max number among three
    max_no= a if a>b else b
    return print("The max number is ",max_no if max_no>c else c)

max_num(2,3,4)
