from replit import clear
#HINT: You can call clear() to clear the output in the console.

bidder_dictionary = {}

def blind_auction():
  
  active_bid = "yes"
  while active_bid == "yes":
    bidder_name = input("Please input your name: ")
    bidder_bid = int(input("\nPlease input your bid: $"))
    bidder_dictionary[bidder_name] = bidder_bid
    active_bid = input("\nAre there more bidders? Type 'yes' or 'no': ")
    clear()

blind_auction()

top_bid = 0
for x in bidder_dictionary:
  if bidder_dictionary[x] > top_bid:
    top_bid = bidder_dictionary[x]

for x in bidder_dictionary:
  if bidder_dictionary[x] == top_bid:
    print(f"{x} has the winning bid at ${top_bid}")

print("\nWould you like to do another auction?\n")
restart = input("Type 'yes' or 'no': ")

if restart == 'yes':
  clear()
  blind_auction()
else:
  print("Goodbye")