path="/var/lib/jenkins/workspace/my_python_job/file10"

print(path)
def stuff(n):
    count = 2
    symbol = "*"
    Coefficient = 19
    index = 1
    while index <= n:
        space = Coefficient * " "
        print(space+(symbol*count))
        Coefficient-=1
        count+=2
        index+=1

with open(path , "w") as x :
    x.write(stuff(20))
