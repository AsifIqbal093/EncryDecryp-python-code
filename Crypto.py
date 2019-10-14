alphabits = 'abcdefghijklmnopqrstvuwxyz'
key = 5
En_msg =''
Dec_msg = ''

''''Condition for continuous iteration'''

while True:
    ''''Taking Input from user'''
    Res = input('Please press A for Encryption or press B for Decryption ')

    ''''Condition checking if user wishes to encrypt text'''
    if Res== 'A':
        msg = input('Please enter a message : ')
        for char in msg:
            position = alphabits.find(char)
            new_position = (position + key)%26
            new_char = alphabits[new_position]
            En_msg += new_char

        print('Your Message was :' + msg)
        print('Encrypted message is :' + En_msg)


    '''Condition checking if user wishes to decrypt text'''
    elif Res=='B':
        msg = input('Please enter a message : ')
        for char in msg:
            position = alphabits.find(char)
            new_position = (position - key)%26
            new_char = alphabits[new_position]
            Dec_msg += new_char
        print('Your Message was :' + msg)
        print('Decrypted message is :' + Dec_msg)

    '''''Notifying for a valid entry''''
    else :
        print('please enter a valid response')
        continue
    '''''Checking whther user wants to exit or continue'''''
    Rep = input('If you to Exit, press E , else press any key')
    if (Rep == 'E'):
    break
    else:
    continue
    





    


