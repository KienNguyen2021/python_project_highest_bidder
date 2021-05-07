from replit import clear

bids ={}
bidding_finished = False

def find_highest_bidder (bidding_record):

# a dict : {" Tom" : 100, "John" : 200, "Jack": 300,}
# bidding_record = {" Tom" : 100, "John" : 200, "Jack": 300,}
# use FOR LOOP in dictionary to go through bidding_record, name of bidder is the key

  highest_bid = 0    # to declare a variable to keep track of highest bid

  winner = " "      # to declare a winner value string

  for bidder in bidding_record :
    bid_amount = bidding_record [bidder]

    if bid_amount > highest_bid :
           highest_bid  = bid_amount
           winner = bidder           # bidder here is the key of dictionary

  print(f"The winner is {winner} with a bid of $ {highest_bid}")   

while not bidding_finished :

    name = input ("What is your name : ?")
    price = int(input("what is your bid : ? $"))  
     # the value of input is string, int convert into number

    bids [name] = price     # this creates a dictionary with name key, price is value

    should_continue= input(" Are there any other bidders ? Type 'Yes' or 'No'.\n")

    if should_continue == "no" :

       bidding_finished = True
       find_highest_bidder (bids)    # calling function find_highest_bid to pass 1 parameter bids

    elif  should_continue == "yes":
       clear ()
