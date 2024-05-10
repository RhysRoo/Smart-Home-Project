import tkinter
from backend import SmartHome, SmartOven, SmartPlug
from tkinter import *

homeManagement = SmartHome()

def setupHome():
    """sets up the home"""
    homeManagement.addDevice(SmartOven())
    homeManagement.addDevice(SmartOven())
    homeManagement.addDevice(SmartOven())
    homeManagement.addDevice(SmartPlug())
    homeManagement.addDevice(SmartPlug())

setupHome()

def main():
    def GUI():
        """creates the GUI"""
        mainWin = Tk()
        mainWin.title("Smart Home")
        mainWin.geometry("450x{}+100+100".format(((len(homeManagement.getDevices()) * 35) + 100)))
        mainWin.resizable(width=False, height=False)
        mainWin.columnconfigure(index=0, weight=1)
        mainWin.columnconfigure(index=1, weight=0)
        mainWin.columnconfigure(index=2, weight=0)

        # Widgets

        def turnAllOnCmd():
            """turns all devices on"""
            homeManagement.turnOnAll()
            displayAllDevices(mainWin)
            mainloop()

        turnAllOnBTN = Button(mainWin, text="Turn all on", command=turnAllOnCmd)
        turnAllOnBTN.grid(row=1, column=0, sticky= "w")
        if len(homeManagement.getDevices()) == 0:
            addSmartPlugBtn = Button(mainWin, text="Add Plug") # adds a new SmartPlug device
            addSmartPlugBtn.grid(row=1, column=3, sticky="e")

            addSmartPlugBtn = Button(mainWin, text="Add Oven") # adds a new SmartPlug device
            addSmartPlugBtn.grid(row=2, column=3, sticky="e")

        def turnAllOffCmd():
            """turns all devices off"""
            homeManagement.turnOffAll()
            displayAllDevices(mainWin)

        turnAllOffBTN = Button(mainWin, text="Turn all off", command=turnAllOffCmd) # Button to turn all devices off
        turnAllOffBTN.grid(row=2, column=0, sticky= "w")

        displayAllDevices(mainWin)

        mainWin.mainloop()

    def displayAllDevices(mainWin):
        """"displays all devices"""
        for i in range(len(homeManagement.getDevices())):  # this loop creates the buttons and labels for each device

            objectText = Text(mainWin, height=1, width=80)  # creates a text box for each device
            objectText.grid(row=i + 3, column=0, padx=0, pady=5)

            objectText.insert(END, homeManagement.getDeviceAt(i))   # inserts the device into the text box

            def addSmartPlugCmd():
                """Button that adds a new SmartPlug device """
                homeManagement.addDevice(SmartPlug())
                displayAllDevices(mainWin)
                mainWin.destroy()
                GUI()

            addSmartPlugBtn = Button(mainWin, text="Add Plug", command=addSmartPlugCmd) # adds a new SmartPlug device
            addSmartPlugBtn.grid(row=1, column=3, sticky="e")

            def addSmartOvenCmd():
                """Button that adds a new SmartOven device """
                homeManagement.addDevice(SmartOven())
                displayAllDevices(mainWin)
                mainWin.destroy()
                GUI()

            addSmartOvenBtn = Button(mainWin, text="Add Oven", command=addSmartOvenCmd) # adds a new SmartOven device
            addSmartOvenBtn.grid(row=2, column=3, sticky="e")

            def modifyDeviceWin():
                """modifies the selected device"""
                modifyWin = tkinter.Toplevel()
                modifyWin.title("Modify Device")
                modifyWin.geometry("200x100")
                modifyWin.resizable(width=False, height=False)

                def removeDevice(index):
                    """removes the selected device"""
                    homeManagement.removeDeviceAt(index)
                    modifyWin.destroy()
                    displayAllDevices(mainWin)
                    mainWin.destroy()
                    GUI()

                removeBtn = Button(modifyWin, text="Remove device", command=removeDevice)   # removes the selected device
                removeBtn.grid(row=1, column=0, sticky="w")

                def closeWin():
                    """closes the window of modifyDeviceWin"""
                    winButtonClose = Button(modifyWin, text="Close", command=modifyWin.destroy)
                    winButtonClose.grid(row=1, column=1, sticky="e")
                closeWin()

                modifyWin.grab_set() # prevents the user from interacting with the main window while the modify window is open
                modifyWin.mainloop()

            modifyBtn = Button(mainWin, text="Modify device", command=modifyDeviceWin)  # Button to open modify window
            modifyBtn.grid(row=i+3, column=3, sticky="e")

            def updateText(index=i, text=objectText):
                """updates the text"""
                update(index, text)

            objectBTN = Button(mainWin, text="Toggle this", command=updateText) # Button to toggle the device
            objectBTN.grid(row=i + 3, column=1, padx=0, pady=5)

    def update(index, text):
        """updates the text"""
        homeManagement.toggleSwitch(index)
        text.delete(1.0, END)   # deletes the text in the text box
        text.insert(END, homeManagement.getDeviceAt(index)) # inserts the updated device into the text box
    GUI()

#Excution of the program
main()
