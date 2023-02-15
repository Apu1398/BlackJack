import secrets

cards = {"A": [1,11], "2":2, "3":3, "4":4,"5":5, "6":6, "7":7,"8":8, "9":9, "10":10,"J":10, "Q":10, "K":10}
cardsUsed = []

types = ["C", "D", "T", "P"]
players = []


def generateRandomCard():

    card =  {"type": secrets.choice(types), "value": secrets.choice(list(cards.items()))}
    #cardsUsed.append(list(card))

    return card


def createPlayers():

    numberOfPlayers = int("Enter the number of players: ")

    

    for player in range(numberOfPlayers):
        firstCard = generateRandomCard()
        secondCard = generateRandomCard()
        print("Cards of player number " + str(player) + ": " + firstCard["type"] + "," + firstCard["value"] + " -- " + secondCard["type"] + "," + secondCard["value"] )
        players.append([player, firstCard, secondCard])


def main():

    for player in players:

        print("Turn player number " + str(player[0] + 1))

        extraCard = input("Do you want an extra card? Type   1->Yes      0->No")

        while extraCard == "1":
            player.append(generateRandomCard())
            extraCard = input("Do you want an extra card? Type   1->Yes      0->No")

            



    return 0


