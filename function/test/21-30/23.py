def coin_changer(amount):
    coin_list = ['1000', '500', '100', '50', '10', '5', '2', '1']
    coin_dict = {'1000' : 0, '500' : 0, '100' : 0, '50' : 0, '10' : 0, '5' : 0, '2' : 0, '1' : 0}
    for c in coin_list:
        if amount == 0:
            break
        else:
            n_coin = amount // int(c)
            coin_dict[c] = n_coin
            amount -= n_coin * int(c)
    return coin_dict

print(coin_changer(21535))            