def encoder(message):
    message_arr = [char for char in message]
    split_message_arr = []
    word = ''

    for i in range(len(message_arr)-1):
        
        if message_arr[i] == message_arr[i+1]:
            word += message_arr[i]
            if i == len(message_arr) - 2:
                word += message_arr[i+1]
                split_message_arr.append(word)
        else: 
            word += message_arr[i]
            split_message_arr.append(word)
            word = ''
   
    encoded_message = ''

    for item in split_message_arr:
        if len(item) > 1:
            encoded_message += f'{len(item)}{item[0]}'
        else:
            encoded_message += item[0]   
    return encoded_message



def decoder(message):
    decoded_message = ''
    split_massage_arr = []
    message_arr = [char for char in message]
    for i in range(len(message_arr)):
        if message_arr[i].isdigit():
            split_massage_arr.append(message_arr[i])
            decoded_message += message_arr[i+1]* int(message_arr[i])
        elif i >= 1 and message_arr[i].isalpha() and message_arr[i - 1].isalpha():
            decoded_message += message_arr[i]
    return decoded_message



print(encoder('aabbccc')) # -> 2a2b3c
print(encoder('aa bb ccc')) # -> 2a 2b 3c

print(decoder('2a')) # -> aa
print(decoder('3a4b')) # -> aaabbbb
print(decoder('3ad4c')) # -> aaadcccc


