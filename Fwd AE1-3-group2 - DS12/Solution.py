
import sys
def programmenu():
    print('{:*^100}'.format(" * "))
    column1 = ["1 ENCRYPT","2 DECRYPT","3  EXIT"]
    for c1 in zip(column1):
        print ("%-15s  " % (c1))
    print('{:*^100}'.format(" * "))
    choic=int((input("Enter your choice \t")))
    return choic


def cipher_key():
    print("cipherky must contain each letter of A-Z exactly once, no letter should repeat itself")
    cipherky = input("Enter cipherky: ").upper()
    for i in range(len(cipherky)):
        pos = i
        for j in range(len(cipherky)):
            if pos == j:
                
                continue
            elif cipherky[i] == cipherky[j]:
                print("Letter {} repeating in cipherky".format(cipherky[i]))
                sys.exit()

    temp = ""
    for i in range(len(cipherky)):
        temp += cipherky[i]
    for i in range(26):
        temp += chr(i+65)

    ke_with_key = ""
    for i in range(len(temp)):
        found = False
        for j in range(len(ke_with_key)):
            if temp[i] == ke_with_key[j]:
                found = True
                break
            # if
        # inner for
        if not found:
            ke_with_key += temp[i]


    return ke_with_key


def msg_encryptfunc(key1, ke):
    usr_msg = input("Enter your message: ").upper()

    enc_result_txt = ""
    for i in range(len(usr_msg)):
        if usr_msg[i] == chr(32):
            enc_result_txt += " "
        else:
            counter = 0
            for j in range(len(ke)):
                if usr_msg[i] == ke[j]:
                    enc_result_txt += key1[counter]
                    break
                else:
                    counter += 1

    print("Encrypted Result: {}".format(enc_result_txt))


def decrypt_func(key1, ke):
    usr_msg = input("Enter Message to decrypt: ").upper()

    decrypted_text = ""
    for i in range(len(usr_msg)):
        if usr_msg[i] == chr(32):
            decrypted_text += " "
        else:
            counter = 0
            for j in range(len(ke)):
                if usr_msg[i] == key1[j]:
                    decrypted_text += ke[counter]
                    break
                else:
                    counter += 1

    print("Decrypted Text: {}".format(decrypted_text))


def main():
    ke = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key1 = cipher_key()
    loop = 1
    choice = 0
    while loop == 1:
        choice = programmenu()
        if choice == 1:
            print("---Encryption---")
            msg_encryptfunc(key1, ke)
        elif choice == 2:
            print("---Decryptioin---")
            decrypt_func(key1, ke)
        elif choice == 3:
            print("Exiting!!! Bye")
            loop = 0
        else:
            print("Incorrect Choice!! Please Select among the given")

if __name__ == "__main__":
    main()