# Function to swap two numbers (by reference via mutable types or tuple return). 
def swp_num(x,y):
    print("before swap the number",x,y)
    temp = x
    x = y
    y = temp
    print("after the swap value of ",x, "and",y)
swp_num(10,20)
