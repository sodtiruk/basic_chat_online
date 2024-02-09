import socket
import threading
from tkinter import *

def main():
    # Server and port that you want to connect to
    IPSERVER = "localhost"
    PORT = 3333

    #connect server
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((IPSERVER, PORT))

    gui = Tk()    
    gui.title("Chat Online Basic") #set name title
    gui.geometry("600x700") 
    # gui.resizable(False, False)

    textBoxReadChat = Text(gui, height=20, width=80, font=("Helvetica", 20))
    textBoxTypeChat = Text(gui, height=10, width=20, font=("Helvetica", 32))    
    buttonSendChat = Button(gui, text="Send", command=lambda: sendMessageToServer(textBoxTypeChat, textBoxReadChat),width=40, height=40)

    #position widget
    textBoxReadChat.pack()
    textBoxTypeChat.pack(side=LEFT)
    buttonSendChat.pack(side=RIGHT)

    #bind keyboard enter and send
    #when you press enter from your keyboard you will be able to send the message
    gui.bind("<Return>", lambda event: sendMessageToServer(textBoxTypeChat, textBoxReadChat))
    

    gui.mainloop()
    # client.close()
    
def sendMessageToServer(textType, textRead):
    # client.sendall(b'Hello world')

    #clear texttype to send message
    message = str(textType.get("1.0", END))
    textType.delete("1.0", END)
    #delte space text
    clearMessage = message.strip()
    print(clearMessage)

    #message you on textbox
    textRead.insert(END, f"> {clearMessage}\n")

    #send message to server


def readMessageFromServer():
    pass


if __name__ == "__main__":
    main()


