class Dzivnieks:
    def __init__(self, vards, skana):
        self.vards = vards
        self.skana = skana
    
    def izvada_dzivnieku(self):
        return f"{self.vards} saka {self.skana}!"
    
govs = Dzivnieks("govs", "mū")
pupukis = Dzivnieks("putns", "pupukū")


print(govs.izvada_dzivnieku())