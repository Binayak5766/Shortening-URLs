from tkinter import *
import random
import string
from postgresql import add_to_table, search_through_shortlink
from chrome import Search

class Outline(object):

	def __init__(self, window):
		l1 = Label(window, text="URL Shortner")
		l1.grid(row=0, column=0, columnspan=6)

		self.url = StringVar()
		self.url_enter = Entry(window, textvariable=self.url)
		self.url_enter.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

		self.output = StringVar()
		self.url_output = Entry(window, textvariable=self.output)
		self.url_output.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

		butn = Button(window, text="Create URL", width=12, command=self.generate)
		butn.grid(row=3, column=0, pady=5, padx=5)

		butn2 = Button(window, text="Exit", width=12, command=window.destroy)
		butn2.grid(row=4, column=0, padx=5, pady=5)

		butn3 = Button(window, text="Search", width=12, command=self.search)
		butn3.grid(row=5, column=0, padx=5, pady=5)


	def generate(self):
		url = self.url_enter.get()
		small = string.ascii_letters + string.digits
		result_str = ''.join(random.choice(small) for i in range(8))
		result_str = 'https://binayak.5766/' + result_str
		add_to_table(url, result_str)
		self.url_output.delete(0,END)
		self.url_output.insert(END,result_str)

	def search(self):
		string = search_through_shortlink(self.url_output.get())
		Search(string)


window = Tk()
Outline(window)
window.mainloop()