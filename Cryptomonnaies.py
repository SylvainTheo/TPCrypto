import requests

def askCurrency():
    monnaie = input("Indiquez l'abréaviation de la crypto-monnaie dont vous désirez connaitre le prix. Taper q pour quitter !\nVotre réponse : ")
    if monnaie != "q":
        showValue(monnaie)

def showValue(monnaie):
    req = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+monnaie+'&tsyms=BTC,USD,EUR').json()
    print("Votre monnaie vaut : "+str(req["EUR"])+" euros, "+str(req["BTC"])+" de Bitcoin, "+str(req["USD"])+".")
    askCurrency()

def main():
    try:
        req = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()["Data"]
        for value in req.values():
            print(value['FullName'])
        askCurrency()    
    except:
        print("Erreur lors de la récupération des noms des crypto-monnaies !")
        askCurrency()

main()