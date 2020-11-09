
def encryp_func():
    userinput = input("Please enter your message:\n ")
    ciph_key = input("Please enter your ciph_key: \n  ")

    hex_msg_conv = ""
    iter_val = 0
    for i in range(len(userinput)):
        tmp_result = ord(userinput[i]) ^ ord(ciph_key[iter_val])
        # padding single letter hex with 0, so that it can be  two letter pair
        hex_msg_conv += hex(tmp_result)[2:].zfill(2)
        iter_val += 1
        #increasing the iteration value
        if iter_val >= len(ciph_key):
            # After all letters of the ciph_key used, repeating again to encrypt
            iter_val = 0

    print("Encrypted message: {}".format(hex_msg_conv))




def main():
    encryp_func()
    

if __name__ == "__main__":
    main()