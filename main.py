
def mass_tax(item_list):
    price = 0
    tax = 6.25
    for items in item_list:
        price += items
    price_dif = price * (tax / 100)
    total = price + price_dif
    return total

def NH_tax(item_list):
    price = 0
    tax = 6.25
    for items in item_list:
        price += items
    price_dif = price * (tax / 100)
    total = price + price_dif
    return total


def in_dec(item_dic):
    item = None
    test = ['Wic Eligible food',"Clothing"]
    for items in item_dic:
        if items in test:
            item = "good"
        if items not in item_dic:
            item = None
    return item

def check_state(state):
    item = None
    test = ["Massachusetts","New Hampshire","Maine"]
    for items in range(0,len(test)):
        if state not in test:
            return item
        item = "good"
    return item


def item_price(probuct):
    sum = 0
    item = {"apple":4,"banna":2,"breed":3,"shirt":13,"pants":12,"stuffy":8,"cup":6}
    for items in probuct:
        if items not in item:
            return None
        else:
            sum += item[items]
    return sum


#state,item_dic


def main(state,item_dic):
    check_items = in_dec(item_dic)




   # if state == "Massachusetts":
      #  price = mass_tax(item_list)



