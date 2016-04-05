 # -*- coding: utf-8 -*-
def handla(nummer,betalt):
    listofprice = ([])

    if nummer == 1:
        price = 10
        thegoodstuff = "choklad"
    if nummer == 2:
        price = 8
        thegoodstuff = "festis"
    if nummer == 3:
        price = 5
        thegoodstuff = "kack"
    if nummer == 4:
        price = 15
        thegoodstuff = "bilar"
    delta = betalt - price
    if betalt == price:
        return "tackar för ditt kop"
    if betalt < price:
        return "för lite pengar "
    while delta >= 500:
       delta -= 500
       listofprice.append(500)
    while delta >= 100:
       delta -= 100
       listofprice.append(100)
    while delta >= 50:
        delta -= 50
        listofprice.append(50)
    while delta >= 20:
       delta -= 20
       listofprice.append(20)
    while delta >= 10:
        delta -= 10
        listofprice.append(10)
    while delta >= 5:
       delta -= 5
       listofprice.append(5)
    while delta >= 1:
       delta -= 1
       listofprice.append(1)
    return thegoodstuff, listofprice


print handla(1,20)