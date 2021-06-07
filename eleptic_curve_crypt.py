symb_to_cord = {'с': '(5,1)', 'о': '(5,12)', 'б': '(7,5)', 'щ': '(7,8)',
                'е': '(9,3)', 'н': '(9,10)', 'и': '(10,1)', 'ё': '(10,12)', 'а': '(0,6)', 'в': '(0,7)', 'г': '(11,1)',
                'д': '(11,12)', '': 0}

coord = {'(5,1)': 'с', '(5,12)': 'о', '(7,5)': 'б', '(7,8)': 'щ',
         '(9,3)': 'е', '(9,10)': 'н', '(10,1)': 'и', '(10,12)': 'ё', '(0,6)': 'a', '(0,7)': 'в', '(11,1)': 'г',
         '(11,12)': 'д', 0: ''}

s_G = {1: '(5,1)', 2: '(7,8)', 3: '(10,1)', 4: '(11,12)', 5: '(0,6)',
       6: '(9,3)', 7: '(9,10)', 8: '(0,7)', 9: '(11,1)', 10: '(10,12)', 11: '(7,5)', 12: '(5,12)', 0: 0}

cord_G = {'(5,1)': 1, '(7,8)': 2, '(10,1)': 3, '(11,12)': 4, '(0,6)': 5,
          '(9,3)': 6, '(9,10)': 7, '(0,7)': 8, '(11,1)': 9, '(10,12)': 10, '(7,5)': 11, '(5,12)': 12, 0: 0}

for_minus = {'(0,6)': '(0,7)', '(0,7)': '(0,6)', '(5,1)': '(5,12)', '(5,12)': '(5,1)', '(7,5)': '(7,8)',
             '(7,8)': '(7,5)', '(9,3)': '(9,10)', '(9,10)': '(9,3)', '(10,1)': '(10,12)', '(10,12)': '(10,1)',
             '(11,1)': '(11,12)', '(11,12)': '(11,1)'}

secret_key_KN = 6
secret_key_SM = 8
general_secret_key = (secret_key_KN * secret_key_SM) % 13
session_key = 3
print('Открытый ключ Каляса ёпта:', s_G.get(secret_key_KN))
print('Открытый ключ Михана бля:', s_G.get(secret_key_SM))
print('Общий секретный ключ:', s_G.get(general_secret_key))

# сайфер блак

message = "гавно"


def preprocessing(m):
    m = m.replace(" ", "").replace(",", "").replace(".", "").replace("'", "").replace(":", "").replace(";", "")
    m = m.lower()
    return m


message = preprocessing(message)


def mesToText(m):
    message = []
    for i in range(0, len(m)):
        message.append(m[i])
    return message


mes = mesToText(message)

mes_G = []
for i in mes:
    mes_G.append(cord_G.get(symb_to_cord.get(i)))
encrypted_mes = []
for i in mes_G:
    g = (i + session_key * secret_key_SM) % 13
    encrypted_mes.append(coord.get(s_G.get(g)))
dop_dot = s_G.get(session_key)

print('Зашифрованное сообщение: ')
for i in encrypted_mes:
    print(i, end="")
print('\nДополнительная точка:\n', dop_dot)


decrypted_mes = []
for i in encrypted_mes:
    s_c = symb_to_cord.get(i)
    s_w = (cord_G.get(s_c) + secret_key_SM * cord_G.get(for_minus.get(dop_dot))) % 13
    decrypted_mes.append(coord.get(s_G.get(s_w)))

print('Расшифрованное сообщение: ')
for i in decrypted_mes:
    print(i, end="")
