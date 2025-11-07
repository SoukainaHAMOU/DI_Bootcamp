birth = input("Enter your birthdate (DD/MM/YYYY): ")
birthday = tuple(birth.split("/"))
Day, Month, Year = birthday
age = 2025 - int(Year) 
candles = int(str(age)[1]) 
calcul = int((11 - candles)/2) 
if (int(Year) % 400 == 0) or (int(Year) % 4 == 0 and int(Year) % 100 != 0):
    for i in range(2): 
        print(calcul * ' _', "i" * candles, calcul * '_') 
        print("  |:H:a:p:p:y:|") 
        print('__|___________|__') 
        print('|^^^^^^^^^^^^^^^^^|') 
        print('|:B:i:r:t:h:d:a:y:|') 
        print("|                 |") 
        print("~~~~~~~~~~~~~~~~~~~") 
else: 
    print(calcul * ' _', "i" * candles, calcul * '_') 
    print("  |:H:a:p:p:y:|") 
    print('__|___________|__') 
    print('|^^^^^^^^^^^^^^^^^|') 
    print('|:B:i:r:t:h:d:a:y:|') 
    print("|                 |") 
    print("~~~~~~~~~~~~~~~~~~~")