
user_input=int(input("Please enter a number : "))



def dicto(input):
    dict=[]
    for i in range(0,input+1,1):
        dict.append(i)
    print(dict)
        
    

dicto(user_input)


inp=int(input("Please input an number : "))



def seperate(input):
    even=[]
    odd=[]
    for i in range(1,input+1,1):

        if i%2 == 0:
            even.append(i)

        elif i%2 == 1:
            odd.append(i)
    print(f"The even numbers are {even} and the odd numbers are {odd}.")

seperate(inp)

