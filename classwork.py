# addition
first=int(input("enter the first number "))
second = int(input("enter the second number"))

def addition():
    sum = first+second
    print(f"your sum is : {sum}")
    return sum

addition()

# ask information about laptop
brandname=(input("enter the brand name of your laptop: "))
modelname=(input("enter thhe model name: "))
price=int(input("enter the price of the laptop: "))

def specs():
    print(f"{brandname} {modelname} @ Rs. {price}")

specs()

#working model of an atm machine

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired = False

print("please insert you atm card: ")
required_amt = int(input("please enter a amount"))

def read_card():
    card_details = [1200,False,False]
    total_price = card_details [0]
    is_same_bank = card_details[1]
    is_expired = card_details [2]
    if is_expired is False:
        peform_transaction(total_price,is_same_bank)
    else:
        return "sorry, this card is not accepted here: "

def peform_transaction(total_amt, is_same_bank, required_amt):
    charge= 0
    if not is_same_bank:
        charge = 5
    else:
        if required_amt > total_amt:
            return "not enough balance"
        else:
            
            print(f"remaining available balance: {total_amt-required_amt-charge}")
            return required_amt
    

read_card()




