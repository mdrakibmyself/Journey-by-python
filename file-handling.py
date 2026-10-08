with open("jatri.txt", "w") as f:
    f.write("Rahim\n")
    f.write("Karim\n")
    
with open("./jatri.txt","r") as f:
    lekha = f.read()
    print(lekha)
