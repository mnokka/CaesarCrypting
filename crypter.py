#
# Simple Ceasar crypter-decrypter
# Uses hardcoded shifting value (negative=backwards in letterlist)



#letter to be shifted value
shifter=-4

#alphabets to be used
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]



# Defining main function
def main():
        print("Ceasar Crypter, fixed shifting value:",shifter)
        print("Used alphabet:",letters)
        print ("Number of letters:",len(letters))

        menu()
        
        while True:
            x=input()
        
            if (x=="1"):
                print("Crypting")
                crypt()
            elif (x=="2"):
                print("Decrypting")
                decrypt()
            elif (x=="x"):
                print ("Ending") 
                break   
            else:
                print ("Wrong selection")
                menu()
 
 
def menu():
        print("Select operation")
        print("1-crypt")
        print("2-decrypt")
        print ("x - end") 
        
def crypt():
    word=input("To be crypted:")
    wlen=len(word)
    cryptedword=""
    for i in range(wlen):
        cletter=cryptLetter(word[i])
        cryptedword=cryptedword+cletter
    
    print("Crypted word:",cryptedword)

    
def cryptLetter(letter):
    location=(letters.index(letter))
    alphaslen=len(letters)
    z=location+shifter
    
    # over maximum len
    if (z>=alphaslen):
        positiveover=z-alphaslen
        cryptedletter=letters[positiveover]
    #under location 0
    elif (z<=0):
        negativeover=alphaslen+z
        cryptedletter=letters[negativeover]
    #inside letters range
    else:
        cryptedletter=letters[z]

    return cryptedletter    

def decrypt():  
    word=input("To be decrypted:")
    wlen=len(word)
    decryptedword=""
    for i in range(wlen):
        dletter=decryptLetter(word[i])
        decryptedword=decryptedword+dletter
    
    print("Decrypted word:",decryptedword)

    
def decryptLetter(letter):              
    location=(letters.index(letter))
        
    alphaslen=len(letters)
    z=location-shifter
    
    # over maximum len
    if (z>=alphaslen):
        positiveover=z-alphaslen
        decryptedletter=letters[positiveover]
    #under location 0
    elif (z<=0):
        negativeover=alphaslen+z
        decryptedletter=letters[negativeover]
        #inside letters range
    else:
        decryptedletter=letters[z]

    return decryptedletter    



if __name__=="__main__":
    main()



    
