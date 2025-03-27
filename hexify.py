def main():
    string = input("turn anything into hex:")
    string_byte = string.encode("utf-8")
    hexresult = string_byte.hex()
    print(hexresult)

a = True

while a:
    main()
