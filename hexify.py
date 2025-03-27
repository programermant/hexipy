#start with main() function

#define
def main():
    #get user input to format
    string = input("turn anything into hex:")

    #encode as utf-8 to begin
    string_byte = string.encode("utf-8")

    #actually *convert* utf-8 to hex
    hexresult = string_byte.hex()

    #finally and most importantly;print the result
    print(hexresult)

#set a to true and make a infinite loop
a = True

#the loop
while a:
    main()
