import random
import replit


def card_selection():
  return random.choice(card_deck)


def start_game(deck1, deck2, num_cards):

  for x in range(num_cards):
    deck1.append(card_selection())
  print(f"YOUR DECK:\n{deck1}\n")

  deck2.append(card_selection())
  print(f"DEALER'S DECK:\n{deck2}")


def add_card(deck):
  deck.append(card_selection())


def show_decks(deck1, deck2):
  print(f"YOUR DECK:\n{deck1}\n")
  print(f"DEALER'S DECK:\n{deck2}\n")


def calculate_score(deck):
  score = sum(deck)
  if score > 21:
    if deck.count(11) > 0:
      return score - 10
    else:
      return score
  elif score <= 21:
    return score


def hit_me(deck):

  hit = input("\nDo you want another card? Type 'y' or 'n': ")
  replit.clear()

  if hit == 'y':
    add_card(deck)
    print(f"\n{deck}\n")
    if sum(deck) == 21:
      print(f"You got to {calculate_score(deck)}!\n")
    elif sum(deck) > 21 and deck.count(11) > 0:
      eleven_position = deck.index(11)
      deck[eleven_position] = 1
      hit_me(deck)

    elif sum(deck) > 21 and deck.count(11) == 0:
      return

    else:
      hit_me(deck)

  elif hit == 'n':
    print(f"{deck} your total is {calculate_score(deck)}.")

  return


def reveal_dealer(deck):
  deck.pop(0)  #Removes '?'
  add_card(deck)
  print(f"\nDEALER'S DECK:\n{deck}\n")


def hit_dealer(deck1, deck2):
  total_deck2 = sum(deck2)
  if sum(deck1) > total_deck2 and sum(deck1) <= 21:
    return

  elif sum(deck1) > 21 and deck1.count(11) > 0:
    eleven_position = deck1.index(11)
    deck1[eleven_position] = 1
    hit_dealer(deck1, deck2)

  elif sum(deck1) <= 16:
    add_card(deck1)
    print(f"DEALER DECK:\n{deck1}\n")
    hit_dealer(deck1, deck2)

  return


card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = 'y'
while play_again == 'y':
  print("WELCOME TO BLACKJACK!\n")
  input("PRESS 'ENTER' TO START THE GAME\n")
  replit.clear()

  user_deck = []
  dealer_deck = ["?"]
  start_game(deck1=user_deck, deck2=dealer_deck, num_cards=2)

  hit_me(user_deck)
  reveal_dealer(dealer_deck)
  hit_dealer(dealer_deck, user_deck)

  total_user = sum(user_deck)
  total_dealer = sum(dealer_deck)
  if sum(dealer_deck) > 21 and dealer_deck.count(11) > 0:
    total_dealer = total_dealer - 10
    hit_dealer(dealer_deck, user_deck)

  replit.clear()

  if total_user > 21:
    print(f"YOU LOSE! You went over 21.\n{user_deck}")

  elif total_dealer > 21:
    print(f"YOU WIN! The dealer went over 21\n{dealer_deck}")

  elif total_dealer < total_user:
    print(f"YOUR DECK:\n{user_deck}\n")
    print(f"DEALER'S DECK:\n{dealer_deck}\n")
    print(f"YOU WIN! You had {total_user} and the dealer had {total_dealer}")

  elif total_dealer == total_user:
    print(f"YOUR DECK:\n{user_deck}\n")
    print(f"DEALER'S DECK:\n{dealer_deck}\n")
    print(f"IT'S A TIE! You both had {total_dealer}")

  else:
    print(f"YOUR DECK:\n{user_deck}\n")
    print(f"DEALER'S DECK:\n{dealer_deck}\n")
    print(f"YOU LOSE! You had {total_user} and the dealer had {total_dealer}.")

  play_again = input("Play again? Type 'y' or 'n': ")
  replit.clear()

print("\nTHANKS FOR PLAYING!")
