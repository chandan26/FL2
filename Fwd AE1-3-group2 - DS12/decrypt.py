def decryptfunc():
    userinput = input("Please enter your message:\n")
    ciph_k = input("Please enter your key to Decrypt: \n ")

    convert_decryp = ""
    for i in range(0, len(userinput), 2):
        convert_decryp += bytes.fromhex(userinput[i:i+2]).decode('utf-8')

    decryp_text = ""
    ciph_k_itr = 0
    for i in range(len(convert_decryp)):
        temp = ord(convert_decryp[i]) ^ ord(ciph_k[ciph_k_itr])
        # padding single letter hex with 0, so that it can be  two letter pair
        decryp_text += chr(temp)
        ciph_k_itr += 1
                #increasing the iteration value

        if ciph_k_itr >= len(ciph_k):
            # After all letters of the ciph_key used, repeating again to encrypt
            ciph_k_itr = 0

    print("Decrypted Text: {}".format(decryp_text))

def main():
    try:
        decryptfunc()
    except Exception as error:
        print(" There is some issue with the Key or message")
    

if __name__ == "__main__":
    main()