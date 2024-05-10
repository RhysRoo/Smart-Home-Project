class BassClass:

    def __init__(self):
        self.switchedOn = False

    def getSwitchedOn(self):
        """Returns the switch status of the SmartPlug"""
        return self.switchedOn

    def toggleSwitch(self):
        """Toggles the switch of the SmartPlug"""
        if self.switchedOn == True:
            self.switchedOn = False
        else:
            self.switchedOn = True


class SmartPlug(BassClass):
    """This is SmartPlug class"""

    def __init__(self):
        """Initialises the SmartPlug"""
        super().__init__()
        self.consumptionRate = 0

    def getConsumptionRate(self):
        """Returns the consumption rate of the SmartPlug"""
        return self.consumptionRate

    def setConsumptionRate(self, amount):
        """Sets the consumption rate of the SmartPlug"""
        self.consumptionRate = amount

    def __str__(self):
        """Returns a string representation of the SmartPlug"""
        output = "Plug: "
        if self.switchedOn:
            output += "on"
        else:
            output += "off"
        output += ", {} consumption".format(self.consumptionRate)

        return output

def testSmartPlug():
    """Tests the SmartPlug class"""
    plug = SmartPlug()
    print(plug)  # Switch Status = False, Consumption Rate = 0
    plug.toggleSwitch()  # Switch Status = False
    print(plug.getSwitchedOn())  # True
    print(plug.getConsumptionRate())  # ConsumptionRate = 0
    plug.setConsumptionRate(30)
    print(plug.getConsumptionRate())  # ConsumptionRate = 30
    print(plug)  # Switch Status = True, Consumption Rate = 30

# testSmartPlug()

class SmartOven(BassClass):
    """This is SmartOven class"""

    def __init__(self):
        """Initialises the SmartOven"""
        super().__init__()
        self.temperature = 0

    def getTemperature(self):
        """Returns the temperature of the SmartOven"""
        return self.temperature

    def setTemperature(self, amount):
        """Sets the temperature of the SmartOven"""
        self.temperature = amount

    def __str__(self):
        """Returns a string representation of the SmartOven"""
        output = "Oven: "
        if self.switchedOn:
            output += "on"
        else:
            output += "off"
        output += ", {} degree celsius".format(self.temperature)
        return output

def testSmartOven():
    """Tests the SmartOven class"""
    oven = SmartOven()  # Switch Status = False, Temperature = 0
    oven.toggleSwitch() # Toggle Switch
    print(oven.getSwitchedOn())  # Prints switch status
    print(oven.getTemperature())  # Prints temperature
    oven.setTemperature(260)    # Set Temperature
    print(oven.getTemperature())  # Prints temperature
    print(oven)  # Switch Status = False, Temperature = 260 Degrees Celsius

# testSmartOven()

class SmartHome:
    """This is SmartHome class"""
    def __init__(self):
        """Initialises the SmartHome"""
        self.devices = []

    def getDevices(self):
        """Returns a list of all devices in the SmartHome"""
        return self.devices

    def getDeviceAt(self, index):
        """Takes an index and returns the device at that index"""
        return self.devices[index]

    def addDevice(self, device):
        """Takes a device and adds it to the SmartHome"""
        # smartPlug = SmartPlug() #this variable limited the function so changed it to add more devices
        self.devices.append(device)

    def removeDeviceAt(self, index):
        """Takes an index and removes the device at that index"""
        self.devices.pop(index)

    def toggleSwitch(self, index):
        """Takes an index and toggles the switch of the device on that index"""
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        """Turns on all devices in the SmartHome"""
        for index in range(len(self.devices)):
            if self.devices[index].switchedOn == False:
                self.devices[index].toggleSwitch()

    def turnOffAll(self):
        """Turns off all devices in the SmartHome"""
        for index in range(len(self.devices)):
            if self.devices[index].switchedOn == True:
                self.devices[index].toggleSwitch()

    def __str__(self):
        """Returns a string representation of the SmartHome class"""
        message = "These are all smart home devices:\n"
        output = message.title()

        for device in self.devices:
            output += str(device)
            output += "\n"
        return output

def testHome():
    """Tests the SmartHome class"""
    homeManagement = SmartHome()
    plug1 = SmartPlug()  # adds device to list
    plug2 = SmartPlug()  # adds device to list
    oven1 = SmartOven()  # adds device to list
    plug2.toggleSwitch() #toggles switch
    plug2.setConsumptionRate(45) #sets consumption rate
    oven1.setTemperature(180)   #sets temperature
    homeManagement.addDevice(plug1) #adds device to list
    homeManagement.addDevice(plug2) #adds device to list
    homeManagement.addDevice(oven1) #adds device to list
    print(homeManagement)   #prints all devices
    homeManagement.turnOnAll()  #turns on all devices
    print(homeManagement)   #prints all devices

# testHome()
