# Accessing Values of Dictionaries
list_1 = {	"Bhavin": ["48", "44", "21","23"],
            "Khushit": ["43", "52", "47", "48"],
	        "Sanjay": ["58", "51", "59","61"]}
D1 = {"Cars" : 48, "Auto" : 24, "Bikes": 53}
while True:
    choice = input("1.Want to accesss values of dictionaries into list\n2.Want to access values of list into dictionary \n1/2 :")
    if choice in ("1/2"):    
        if choice == '1':
            values = D1.values()
            value = list
            print(values)
        elif choice == '2':        
            for i in list_1['Khushit']:
                print(i)
            for i in list_1["Bhavin"]:
                print(i)
            for i in list_1["Sanjay"]:
	            print(i)
            
    