class Daneshjo:
    def __init__(self, name, shomare_daneshjoii, reshte):
        self.name = name
        self.shomare_daneshjoii = shomare_daneshjoii
        self.reshte = reshte
        self.nemarat = []

    def ezafe_kardan_nemre(self, nemre):
        self.nemarat.append(nemre)

    def moadel(self):
        if not self.nemarat:
            return 0
        return sum(self.nemarat) / len(self.nemarat)

    def namayesh_ettelaat(self):
        print(f"Name: {self.name}")
        print(f"Shomare Daneshjoii: {self.shomare_daneshjoii}")
        print(f"Reshte: {self.reshte}")
        print(f"Nemarat: {self.nemarat}")
        print(f"Moadel: {self.moadel():.2f}\n")

class Goroh_Daneshjooyan:
    def __init__(self):
        self.daneshjooyan = []

    def ezafe_kardan_daneshjo(self, daneshjo):
        self.daneshjooyan.append(daneshjo)

    def moadel_kelas(self):
        if not self.daneshjooyan:
            return 0
        majmu = sum(d.moadel() for d in self.daneshjooyan)
        return majmu / len(self.daneshjooyan)

    def behtarin_daneshjo(self):
        if not self.daneshjooyan:
            return None
        behtarin = max(self.daneshjooyan, key=lambda d: d.moadel())
        return behtarin

    def namayesh_hame_daneshjooyan(self):
        for d in self.daneshjooyan:
            d.namayesh_ettelaat()

goroh = Goroh_Daneshjooyan()

while True:
    name = input("Name Daneshjo: ")
    shomare = input("Shomare Daneshjoii: ")
    reshte = input("Reshte Tahsili: ")
    daneshjo = Daneshjo(name, shomare, reshte)

    while True:
        voroodi = input("Nemre ya 'payaan' baraye tamam: ")
        if voroodi == "payaan":
            break
        try:
            nemre = float(voroodi)
            daneshjo.ezafe_kardan_nemre(nemre)
        except:
            print("Lotfan adad motabar vared konid")

    goroh.ezafe_kardan_daneshjo(daneshjo)

    edame = input("Daneshjooie digari? (bale/kheir): ")
    if edame != "bale":
        break

goroh.namayesh_hame_daneshjooyan()
print(f"Moadel kol kelas: {goroh.moadel_kelas():.2f}")

behtarin = goroh.behtarin_daneshjo()
if behtarin:
    print(f"Behtarin Daneshjo: {behtarin.name} ba moadel {behtarin.moadel():.2f}")