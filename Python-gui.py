import tkinter

window = tkinter.Tk()

#set width and height
window.geometry("400x200")

youtubeLabel = tkinter.Label(window, text = "youtube URL: ").pack(side = 'left')
enterButton = tkinter.Button(window, text = 'Find song').pack(side = 'right')
inputField = tkinter.Entry(window).pack(side = 'left')



window.mainloop()
