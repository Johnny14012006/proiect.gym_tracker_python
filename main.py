
cnp = input("Introduce CNP-ul: ")

calendar = ["", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", 
            "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]

index_s = cnp[0]

gen = ""
secol = ""

if index_s == '1' or index_s == '2':
    secol = "19" # ar fi fost corect 20 da sa dea bine punem cu 1 in minus
    if index_s == '1':
        gen = "barbat"
    else:
        gen = "femeie"

elif index_s == '3' or index_s == '4':
    secol = "18"
    if index_s == '3':
        gen = "barbat"
    else:
        gen = "femeie"

elif index_s == '5' or index_s == '6':
    secol = "20"
    if index_s == '5':
        gen = "barbat"
    else:
        gen = "femeie"


an_complet = secol + cnp[1:3]

idx_luna = int(cnp[3:5])
luna_text = calendar[idx_luna]
ziua = cnp[5:7]

print(f"Gen: {gen}, Data nasterii: {ziua} {luna_text} {an_complet}")