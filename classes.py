class Human:
    def __init__(self,name) -> None:
        self.name=name
        print("bir yapıcı blok oluşturuldu")
    def talk(self,cumle):
        print(f"{self.name}: {cumle}")
    def walk(self):
        print(f"{self.name} is walking...")

human1=Human("Ahmed")
human1.name="Bilal"
human1.talk("nasılsın?")
human1.name="Önder"
human1.walk()
