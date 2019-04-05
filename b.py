stary = open('ceny_mieszkan_w_poznaniu.tsv', 'r')
sparsowany = open('sparsowane.tsv', 'w')

next(stary)
for i in stary:
    cena, czyNowy, _, pietro, lokacja, metraz = i.rstrip('\n').split('\t')
    wiek = "Nowe" if czyNowy=="True" else "Stare"
    napis = f'Sprzedam {wiek} mieszkanie w dzielnicy {lokacja} na {pietro} piętrze o {metraz} m^2\n'

    sparsowany.write(napis)


