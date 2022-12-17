import random
import replit

def game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  players_hand = []
  computers_hand = []
  
  def deal(hand):
    hand.append(random.choice(cards))
    if sum(hand) > 21 and 11 in hand:
      index = hand.index(11)
      hand[index] = 1
  
  deal(players_hand)
  deal(players_hand)
  
  deal(computers_hand)
  deal(computers_hand)
  
  print(f"Dealer's hand: {computers_hand[1]}")
  print(f"Your hand: {players_hand} -- {sum(players_hand)}")
  
  initial_continue = input("Do you want more cards?\n")
  if initial_continue == 'yes':
    resume = True
  elif initial_continue == 'no':
    resume = False
  else:
    print("Please enter a valid response")
    return
    
  while resume:
    replit.clear()
    deal(players_hand)
    print(f"Dealer's hand: {computers_hand[1]}")
    print(f"Your hand: {players_hand} -- {sum(players_hand)}")
    if sum(players_hand) == 21:
      print("Blackjack! You win!")
      return
    if sum(players_hand) > 21:
      print("Bust")
      return
    should_continue = input("Do you want more cards?\n").lower()
    if should_continue == 'yes':
      continue
    elif should_continue == 'no':
      resume = False
  
  while sum(computers_hand) <= 16:
    deal(computers_hand)
    if sum(computers_hand) == 21:
      print("Dealer wins")
      print(f"Dealer's hand: {computers_hand} -- {sum(computers_hand)}")
      print(f"Your hand: {players_hand} -- {sum(players_hand)}")
      return
    if sum(computers_hand) > 21:
      print("Dealer bust! You win!")
      print(f"Dealer's hand: {computers_hand} -- {sum(computers_hand)}")
      print(f"Your hand: {players_hand} -- {sum(players_hand)}")
      return
      
  print(f"Dealer's hand: {computers_hand} -- {sum(computers_hand)}")
  print(f"Your hand: {players_hand} -- {sum(players_hand)}")
  
  
  if sum(players_hand) > sum(computers_hand):
    print("You win!")
  else:
    print("You lose")

game()
