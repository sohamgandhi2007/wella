class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedlimit=speedlimit

    def start(self):
        print("carstarted")

    def stop(self):
        print("carstopped")

    def accleration(self):
        print("accleration")

    def gear(self):
        print("gearhaschanged")

swift=Car("dzire","white","maruti","180")
swift.start()
swift.stop()
print(swift.model)
print(swift.color)