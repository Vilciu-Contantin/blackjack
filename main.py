############### Proiectul Blackjack #####################

#Dificultate Normală 😎: Folosiți toate sfaturile de mai jos pentru a finaliza proiectul.
#Dificultate Grea 🤔: Folosiți doar Sugestiile 1, 2, 3 pentru a finaliza proiectul.
#Dificultate Extra Grea 😭: Folosiți doar Sfaturile 1 și 2 pentru a finaliza proiectul.
#Expert în dificultate 🤯: Folosiți doar Sugestia 1 pentru a finaliza proiectul.

############### Regulile casei noastre de Blackjack #####################

## Puntea are dimensiuni nelimitate.
## Nu există glumeți.
## Jack/Regina/Regele contează toți ca 10.
## Asul poate conta ca 11 sau 1.
## Folosiți următoarea listă ca pachet de cărți:
## cărți = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## Cărțile din listă au probabilitatea egală de a fi extrase.
## Cărțile nu sunt scoase din pachet pe măsură ce sunt extrase.

#################### Sugestii ####################

#Sfat 1: Accesați acest site web și încercați jocul Blackjack:
# https://games.washingtonpost.com/games/blackjack/
#Atunci, încercați aici proiectul Blackjack finalizat:
# http://blackjack-final.appbrewery.repl.run

#Sfat 2: Citiți această detaliere a cerințelor programului:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Apoi încercați să vă creați propria diagramă de flux pentru program.

#Sfat 3: Descărcați și citiți această diagramă de flux pe care am creat-o:
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Sfat 4: Creați o funcție deal_card() care utilizează Lista de mai jos pentru a *a returna* o carte aleatorie.
#11 este Asul.

import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Sfat 6: Creați o funcție numită calculate_score() care ia o listă de cărți ca intrare
#și returnează scorul.
#Căutați funcția sum() pentru a vă ajuta să faceți acest lucru.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  
# Sfat 7: În interiorul calculate_score() verifică un blackjack (o mână cu doar 2 cărți: as + 10) și returnează 0 în loc de scorul real. 0 va reprezenta un blackjack în jocul nostru.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
# Sugestie 8: În interiorul calculate_score() verificați pentru un 11 (as). Dacă scorul este deja peste 21, eliminați 11 și înlocuiți-l cu 1. Poate fi necesar să căutați append() și remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  

# Sfat 13: Creați o funcție numită compare() și introduceți scorul_utilizator și scorul_calculator. Dacă computerul și utilizatorul au același scor, atunci este egal. Dacă computerul are un blackjack (0), atunci utilizatorul pierde. Dacă utilizatorul are un blackjack (0), atunci utilizatorul câștigă. Dacă user_score este peste 21, atunci utilizatorul pierde. Dacă computer_score este peste 21, atunci computerul pierde. Dacă niciuna dintre cele de mai sus, atunci jucătorul cu cel mai mare scor câștigă.
def compare(user_score, computer_score):

#Rezolvarea unei erori. Dacă tu și computerul sunteți terminați, pierdeți.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
    
    
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  
def play_game():
  
  print(logo)
  
# Sfat 5: Împărțiți utilizatorului și computerului câte 2 cărți folosind deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
# Sfat 11: Scorul va trebui verificat din nou cu fiecare carte nouă extrasă, iar verificările din Sfatul 9 trebuie repetate până la sfârșitul jocului.
  
  while not is_game_over:
   
# Sfat 9: Apelați calculate_score(). Dacă computerul sau utilizatorul are un blackjack (0) sau dacă scorul utilizatorului este peste 21, atunci jocul se termină.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      
# Sugestie 10: Dacă jocul nu s-a încheiat, întreabă utilizatorul dacă vrea să tragă o altă carte. Dacă da, atunci utilizați funcția deal_card() pentru a adăuga un alt card la lista user_cards. Dacă nu, atunci jocul s-a încheiat.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  # Sfat 12: Odată ce utilizatorul a terminat, este timpul să lăsați computerul să se joace. Calculatorul ar trebui să continue să deseneze cărți atâta timp cât are un scor mai mic de 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
#Sfat 14: Întrebați utilizatorul dacă dorește să repornească jocul. Dacă răspund da, șterge consola și începe un nou joc de blackjack și arată sigla de pe art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()