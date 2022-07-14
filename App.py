# I will simulate the problem like this
# J = 11, Q =12, K = 13, A = 14
# Also, the 4 special cards will have the "value" of 15, there is no problem, it's all about simulation
# I will try to make 100K or 1M simulations like this
# I will randomize the deck of card and i will select the player 1. Here , I will check 2 cases
# 1. If he has not even a single one card not in pairs
# 2. If he has not a single pair
from random import shuffle
from timeit import default_timer as timer

# Function 1
def player1Pick():
    # 1. I will create the deck of cards, 4 of every "value"
    cards = list()
    for i in range(2, 16):
        for j in range(4):
            cards.append(i)
    # I will shuffle the cards deck twice for extra randomness
    shuffle(cards)
    shuffle(cards)
    # 2. I will take the first 14 cards of my shuffled list to simulate the 1st player's cards
    # This is like taking 1/4 cards with a certain row, because now we talk about randomness
    player1PickList = cards[0:14]
    # 3. Now, that I have the 14 cards of the 1st player, I will sort my list to make the things easier
    player1PickList = sorted(player1PickList)
    # 4. I will have to exclude 15 = special cards
    for i in range(len(player1PickList), len(player1PickList) - 4, -1):
        if player1PickList[len(player1PickList) - 1 - i] == 15:
            del player1PickList[len(player1PickList) - 1 - i]
    # 5. Now, my list is sorted and does not contain any special cards
    return player1PickList


# Function 2
def checkMonofylla(cards):
    MonofylloExists = False
    # Για να είναι ένα φύλλο σε μία θέση i της λίστας μου μονόφυλλο, θα πρέπει να είναι διαφορετικό
    # και του προηγούμενου και του επόμενου, μιας και τα έχω ταξινομήσει σε αύξουσα σειρά
    # Εξαίρεση αποτελεί η περίπτωση i = 0, η οποία απαιτεί ειδική μεταχείριση
    if cards[0] != cards[1]:
        MonofylloExists = True
    if cards[len(cards)-1] != cards[len(cards)-2]:
        MonofylloExists = True
    for i in range(1, len(cards)-1):
        if cards[i] != cards[i-1] and cards[i] != cards[i+1]:
            MonofylloExists = True
            break
    return MonofylloExists

# Function 3
def checkDifyllies(cards):
    difylliaExists = False
    # I will have to exclude 15 = special cards
    for i in range(len(cards)-1):
        if cards[i] == cards[i+1]:
            difylliaExists = True
            break
    return difylliaExists


# Function 4
def simulate():
    cards = player1Pick()
    flag1 = checkMonofylla(cards)
    flag2 = checkDifyllies(cards)
    return cards, flag1, flag2

# MAIN FUNCTION
print()
start = timer()
LIMIT = 10**5
counter1 = 0
counter2 = 0

for i in range(LIMIT):
    cards, flag1, flag2 = simulate()
    if flag1 == False or flag2 == False:
        print(i, cards, flag1, flag2)
        if flag1 == False:
            counter1 += 1
        if flag2 == False:
            counter2 += 1

end = timer()
elapsed = end - start
elapsed = round(elapsed, 4)
print()
percentage1 = counter1 / LIMIT
print("No Monofylla ----> " + str(counter1) + " / " + str(LIMIT) + " ----> percentage = " + str(100 * percentage1) + "%")
percentage2 = counter2 / LIMIT
print("No Difyllies ----> " + str(counter2) + " / " + str(LIMIT) + " ----> percentage = " + str(100 * percentage2) + "%")
print()
print("Execution time: " + str(elapsed) + " seconds")
# cards = [2, 2, 2, 4, 4, 4, 4, 6, 6, 8, 8, 8, 9, 9]
# print(checkMonofylla(cards))