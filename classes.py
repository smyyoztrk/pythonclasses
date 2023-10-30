class Human:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        print("bir yapıcı blok oluşturuldu")
    def talk(self,cumle):
        print(f"{self.name} {self.age} yaşında, {cumle}")
    def walk(self):
        print(f"{self.name} is walking...")
    def write(self,dokuman):
        print(f"{self.name},bugün {dokuman} yazıyor")

human1=Human("Ahmed",8)
human1.name="Bilal"
human1.talk("nasılsın?")
human1.name="Önder"
human1.walk()
human1.write("makale")
