
#%% 
# Testing While loops for to do app

password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password correct !")

        
# %%
# Hilfestellung in der Konsole

# dir(str) = Liste aller Methoden 
print(dir(str))
# dir("Hello") = ist ein string und gibt auch alle Methoden dazu aus 

# help(methode) oder help("dee".methode) = Sagt dir wsa die Methode genau tut
help(str.capitalize)

# %%
