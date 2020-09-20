import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib

win=tk.Tk()
win.title("PDF To TEXT")

def openFile():
    file=askopenfile(filetypes=[("PDF Files",  "*.pdf")])
    pdf_file=open(file.name, "rb")
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    number_of_pages=read_pdf.getNumPages()
    page=read_pdf.getPage(0)
    page_content=page.extractText()
    pathlib.Path("con_text.txt").write_text(page_content)
    showinfo("Tebrikler", "Ugurla deyisdirildi")

label=tk.Label(win,text="Fayli daxil edin  :  ")
label.grid(row=0,column=0,padx=5,pady=5)

button=ttk.Button(win,text="Deyis",width=30,command=openFile)
button.grid(row=0,column=1,padx=5,pady=5)
win.resizable(False,False)


win.mainloop()
    
