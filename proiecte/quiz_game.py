print("Bine ai venit !")

playing = input("Vrei sa incepi jocul ? ")


if playing.lower() != "da":
    quit()

print("Supeeeer! Hai sa incepem!")

score = 0


answer = input("Care este capitala Turciei? ")

if answer.lower() == "ankara":
    print("Felicitar, ai raspuns corect. ")
    print("Hai sa continuam")

    score = score +1

else:
    print("Incorect!")
    print("Mare pula esti!")
    quit()

answer = input("Care este cel mai lung fluviu din Europa ? ")

if answer.lower() == "volga":
    print("Felicitari, ai raspuns corect!")
    print("Hai sa vedem urmatoarea intrebare")
    score = score + 1
else:
    print("Inocrect!")
    print("Mare pula esti!")
    quit()

answer = input("In ce tara este situat Parndorf ? ")

if answer.lower() == "austria":
    print("Felicitari, ai raspuns corect!")
    print("Hai sa vedem urmatoarea intrebare")
    score = score +1
else:
    print("Incorect!")
    print("Mare pula esti!")
    quit()

answer = input("La ce echipa joaca in prezent Sadio Mane? ")

if answer.lower() == "liverpool":
    print("Felicitari, ai raspuns corect!")
    print("Si ultima intrebare...")
    score = score +1
else:
    print("Incorect!")
    print("Mare pula esti!")
    quit()

answer = input("La cati ani a murit Mihai Eminescu? ")

if answer.lower() == "39":
    print("Felicitari, ai raspuns corect!")
    score = score +1
else:
    print("Incorect!")
    print("Mare pula esti!")
    quit()

print("Felicitari ai raspuns corect la "  + str(score) +  " intrebari!" )
print("Bravo pula")
