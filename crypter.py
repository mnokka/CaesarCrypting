#
# Simple Ceasar crypter-decrypter ,  mika.nokka1@gmail.com Jan 2023
# Uses defined letters array. Not defined letters in tobe-crypted message will be set as ?
# Shifting value: negative=backwards in letterlist,positive forward. 0 does not crypt at all.
#



#letters to be used
letters=[" ",".","1","2","3","4","5","6","7","8","9","0","-","?",
         "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö",
         "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Å","Ä","Ö"]




def main():

        #initial crypting shifter value 
        shifter=-4 
        
        print("Ceasar Crypter, Current shifter value:",shifter)
        print("Used alphabet:",letters)
        print("Number of letters:",len(letters))

        menu(shifter)
        
        while True:
            x=input("?")
        
            if (x=="1"):
                crypt(shifter)
                menu(shifter)
            elif (x=="2"):
                decrypt(shifter)
                menu(shifter)
            elif (x=="3"):
                shifter=changeshifter(shifter)
                menu(shifter)                    
            elif (x=="x"):
                break   
            else:
                print ("Wrong selection")
                menu(shifter)
 
 
def menu(shifter):
        print("")
        print("*********** Select operation *************")
        print("1 - Crypt")
        print("2 - Decrypt")
        print("3 - Crypting shifter value (current:",shifter,")")
        print("x - Quit") 
        
        
def crypt(shifter):
    word=input("String to be crypted:")
    wlen=len(word)
    cryptedword=""
    for i in range(wlen):
        cletter=cryptLetter(word[i],shifter)
        cryptedword=cryptedword+cletter
    print("Crypted:",cryptedword)

    
def cryptLetter(letter,shifter):
    
    #not defined letters , force set as ?
    if letter not in letters:
        letter="?"
    
    location=(letters.index(letter))
    alphaslen=len(letters)
    z=location+shifter
    
    
    #over maximum len
    if (z>=alphaslen):
        positiveover=z-alphaslen
        cryptedletter=letters[positiveover]
    #under location 0
    elif (z<0):
        negativeover=alphaslen+z
        cryptedletter=letters[negativeover]
    #inside letters range
    else:
        cryptedletter=letters[z]
    return cryptedletter    

def decrypt(shifter):  
    word=input("String to be decrypted:")
    wlen=len(word)
    decryptedword=""
    for i in range(wlen):
        dletter=decryptLetter(word[i],shifter)
        decryptedword=decryptedword+dletter    
    print("Decrypted:",decryptedword)

    
def decryptLetter(letter,shifter):              
    location=(letters.index(letter))     
    alphaslen=len(letters)
    z=location-shifter
    
    #over maximum len
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

def changeshifter(shifter):
    print ("*************************************************************")
    print("Used alphabets:",letters)
    print ("Number of letters:",len(letters))
    print("Current crypter letter shifter value:",shifter)
    print ("(Value 0; no crypting done)")
    shifter=input("New shifter value?")
    return int(shifter)

if __name__=="__main__":
    main()



    
