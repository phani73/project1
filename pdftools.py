from tkinter import *
from tkinter import scrolledtext # for the scrool bar window
from tkinter import filedialog, messagebox # opening the filedialog and message box
from PIL import Image
#for inserting the image
from docx2pdf import convert   #word to pdf
#used for conversion
from fpdf import FPDF
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Page4:
    def __init__(self, create_window1):
        self.create_window1 = create_window1
        self.create_window1.geometry('925x500+300+100')
        self.create_window1.resizable(False, False)
        self.create_window1.title('Setting button')
        
        #for settings page
        def load_settings():
            try:
                with open("settings.txt", "r") as f:
                    lines = f.readlines()
                    username = lines[0].strip().split(": ")[1]
                    password = lines[1].strip().split(": ")[1]
                    username_label.config(text=f"Username: {username}")
                    password_label.config(text=f"Password: {password}")
            except FileNotFoundError:
                pass

        load_settings()

        
#class used for all the proccessing


class Page5:
    def __init__(self, create_window2):
        self.create_window2 = create_window2
        self.create_window2.geometry('925x500+300+100')
        self.create_window2.resizable(False, False)
        self.create_window2.title('Help button')

class Page3:
    def __init__(self, create_window):
        self.create_window = create_window
        self.create_window.geometry('925x500+300+100')
        self.create_window.resizable(False, False)
        self.create_window.title('Home button')

class Page2:
    def __init__(self, window):
        self.window = window
        self.window.geometry('925x500+300+100')
        self.window.resizable(False, False)
        self.window.title('Home page')

        # list to store the history 
        self.conversion_history = []

        def hide_indicators():
            home_indicate.config(bg='#ccccff')
            settings_indicate.config(bg='#ccccff')
            history_indicate.config(bg='#ccccff')
            about_indicate.config(bg='#ccccff')

        def indicate(lb):
            hide_indicators()
            lb.config(bg='black')
            
        #all the buttons  and frames  used

        
        main_frame = Frame(window, background='#ccccff', highlightbackground='black', highlightthickness=2)
        
        home_btn = Button(main_frame, text='Home', font=('Bold', 15), fg='black', bd=0, bg='#ccccff', command=lambda: (indicate(home_indicate), createpage()))
        
        home_btn.place(x=100, y=100)

        home_indicate = Label(main_frame, text='', bg='#ccccff')
        home_indicate.place(x=3, y=100, width=5, height=40)

        settings_btn = Button(main_frame, text='Settings', font=('Bold', 15), fg='black', bd=0, bg='#ccccff', command=lambda: (indicate(settings_indicate), createpage2()))
        
        settings_btn.place(x=100, y=170)

        settings_indicate = Label(main_frame, text='', bg='#ccccff')
        settings_indicate.place(x=3, y=170, width=5, height=40)

        history_btn = Button(main_frame, text='History', font=('Bold', 15), fg='black', bd=0, bg='#ccccff', command=lambda: (indicate(history_indicate), show_history()))
        
        history_btn.place(x=100, y=240)

        history_indicate = Label(main_frame, text='', bg='#ccccff')
        history_indicate.place(x=3, y=240, width=5, height=40)

        about_btn = Button(main_frame, text='Help', font=('Bold', 15), fg='black', bd=0, bg='#ccccff', command=lambda: (indicate(about_indicate), createpage3()))
        
        about_btn.place(x=100, y=320)

        about_indicate = Label(main_frame, text='', bg='#ccccff')
        about_indicate.place(x=3, y=320, width=5, height=40)

        main_frame.pack(side=LEFT)
        main_frame.pack_propagate(False)
        main_frame.place_configure(width=300, height=500)

    def add_conversion_history(self, conversion_type, file_name):
        self.conversion_history.append(f"{conversion_type}: {file_name}")
 
#  main page
def page():
    window = Tk()
    global page2_instance
    page2_instance = Page2(window)  # Create an instance of Page2
    label2 = Label(window, text="CLICK\n\n\n ANY OF THE\n\n\nMENU", font=("Arial", 30))
    label2.place(x=450, y=50)
    window.mainloop()
    
# second page

def createpage2():
    create_window1 = Tk()
    create_window1.geometry('925x500+300+100')
    create_window1.resizable(False, False)
    create_window1.title("Setting button")

    
    #function declaration in settings

    
    def save_settings():
        new_username = user_entry.get()
        new_password = password_entry.get()
        with open("settings.txt", "w") as f:
            f.write(f"Username: {new_username}\n")
            f.write(f"Password: {new_password}\n")
        messagebox.showinfo("Success", "Settings saved successfully!")

    def load_settings():
        try:
            with open("settings.txt", "r") as f:
                lines = f.readlines()
                username = lines[0].strip().split(": ")[1]
                password = lines[1].strip().split(": ")[1]
                user_entry.delete(0, END)
                password_entry.delete(0, END)
                user_entry.insert(0, username)
                password_entry.insert(0, password)
        except FileNotFoundError:
            pass

# for  the username and password


    user_label = Label(create_window1, text="Username:", font=("Verdana", 15))
    user_label.place(x=300, y=50)
    user_entry = Entry(create_window1, font=("Arial", 15),bg="#ccccff",foreground="black")
    user_entry.place(x=450, y=50)
    

    password_label = Label(create_window1, text="Password:", font=("Arial", 15))
    password_label.place(x=300, y=130)
    password_entry = Entry(create_window1, show="*", font=("Arial", 15),bg="#ccccff",foreground="black")
    password_entry.place(x=450, y=130)
    

    load_settings_button = Button(create_window1, text="Load Settings", font=("Arial", 15),bg="#ccccff", command=load_settings)
    load_settings_button.place(x=300, y=200)
    

    save_settings_button = Button(create_window1, text="Save Settings", font=("Arial", 15),bg="#ccccff", command=save_settings)
    save_settings_button.place(x=500, y=200)
    

    load_settings()


    create_window1.mainloop()

  

    
# another page


def createpage3():
    create_window2 = Tk()
    create_window2.geometry('925x500+300+100')
    create_window2.resizable(False, False)
    create_window2.title("Help button")
    help_text = """
    Welcome to the Help Page!

    Here are some instructions for using this program:

    1. After login to the page open home to convert any document to pdf\n
    2. First, for example, click on the pdf to word button you can see the\n file dialog opening and select and save the document\n 
    3. You can see the documents in the path you have saved

    For further assistance, please contact 9390655062 or poojithchinnu7@gmail.com.
    """

    help_label = Label(create_window2, text=help_text, width=100, height=100, font=("Arial", 15), fg="white", bg='#ccccff')
    help_label.config(state=DISABLED)
    help_label.pack(padx=10, pady=10)

# displaying the history


def show_history():
    history_window = Tk()
    history_window.geometry('925x500+300+100')
    history_window.resizable(False, False)
    history_window.title('History')

    # Retrieve the conversion history from the Page2 instance
    
    history_list = page2_instance.conversion_history

    # Create a scrolled text widget to display the history


    history_text = scrolledtext.ScrolledText(history_window, wrap=WORD, width=100, height=40,font=("Arial",15))
    history_text.pack(padx=30, pady=30)

    # Populate the history_text widget with the history data

    
    for item in history_list:
        history_text.insert(END, item + '\n')

    history_window.mainloop()

    
# another page after mainpage


def createpage():
    create_window = Tk()
    create_window.geometry('925x500+300+100')
    create_window.resizable(False, False)
    create_window.title("Home button")
  

    label1 = Label(create_window, text="Convert in your Own Way", font=("Bold", 18))
    label1.pack()

 

    
    # word to pdf  conversion function

    
    def word_to_pdf():
        word_file = filedialog.askopenfilename(filetypes=[('Word Documents', '*.docx')])
        if word_file:
            pdf_file = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')])
            if pdf_file:
                try:
                    convert(word_file, pdf_file)
                    page2_instance.add_conversion_history("Word to PDF", pdf_file)
                    messagebox.showinfo("Conversion Complete", "Word Document converted to PDF successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    convert_button = Button(create_window, text="WORD to PDF", command=word_to_pdf, width=12, height=3, font=('Bold', 15), bg='#ccccff', fg='white')
    convert_button.place(x=50, y=50)

    
    # merging two or more pdf 
    def merge_pdfs():
       
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if file_paths:
            merger = PdfMerger()

         
            for path in file_paths:
                merger.append(path)

            # Save merged PDF file
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if save_path:
                merger.write(save_path)
                merger.close()
                page2_instance.add_conversion_history("Merge PDF", save_path)
                messagebox.showinfo("Conversion Complete", "PDF merged successfully!")

    convert_button3 = Button(create_window, text="MERGE PDF", command=merge_pdfs, width=12, height=3, font=("bold", 15), bg='#ccccff', fg='white')
    convert_button3.place(x=50, y=200)

    
     # converting multiple images to pdf

     
    def select_images():
        filetypes = (("JPEG Files", "*.jpg"), ("PNG Files", "*.png"), ("All Files", "*.*"))
        image_files = filedialog.askopenfilenames(title="Select Images", filetypes=filetypes)
        if image_files:
            convert_to_pdf(image_files)

    convert_button2 = Button(create_window, text="Multiple\n images to pdf", command=select_images, width=12, height=3, font=("Bold", 15), bg='#ccccff', fg='white')
    
    convert_button2.place(x=300, y=50)

    
# for the function of selecting images
    def convert_to_pdf(image_files):
        output_file = filedialog.asksaveasfilename(title="Save PDF", defaultextension=".pdf")
        if output_file:
            pdf = FPDF()
            for image_file in image_files:
                image = Image.open(image_file)
                if image.mode != "RGB":
                    image = image.convert("RGB")
                pdf.add_page()
                pdf.image(image_file, 0, 0, pdf.w, pdf.h)
            pdf.output(output_file, "F")
            page2_instance.add_conversion_history("Images to PDF", output_file)
            messagebox.showinfo("Conversion Complete", "Images converted to PDF successfully!")

# converting the excel to pdf


    def excel_to_pdf():
        excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])

        if excel_file:
            pdf_file = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')])
            if pdf_file:
                try:
                    # Convert Excel to PDF logic here
                    page2_instance.add_conversion_history("Excel to PDF", pdf_file)
                    messagebox.showinfo("Conversion Complete", "Excel Document converted to PDF successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    convert_button1 = Button(create_window, text=" Excel to PDF", command=excel_to_pdf, width=12, height=3, font=("Bold", 15), bg='#ccccff', fg='white')
    convert_button1.place(x=300, y=200)

# converting the png to pdf

    def png_to_pdf():
        png_file = filedialog.askopenfilename(filetypes=[('PNG Files', '*.png')])

        if png_file:
            pdf_file = png_file.replace('.png', '.pdf')
            image = Image.open(png_file)
            width, height = image.size
            c = canvas.Canvas(pdf_file, pagesize=(width, height))
            c.drawImage(png_file, 0, 0, width, height)
            c.save()
            page2_instance.add_conversion_history("PNG to PDF", pdf_file)
            messagebox.showinfo("Conversion Complete", f"PNG converted to PDF: {pdf_file}")

    convert_button5 = Button(create_window, text="PNG to PDF", command=png_to_pdf, width=12, height=3, font=("Bold", 15), bg='#ccccff', fg='white')
    convert_button5.place(x=550, y=50)


# converting the jpg image to pdf 
    def jpg_to_pdf():
        jpg_file = filedialog.askopenfilename(filetypes=[('JPG Files', '*.jpg')])

        if jpg_file:
            pdf_file = jpg_file.replace('.jpg', '.pdf')
            image = Image.open(jpg_file)
            width, height = image.size
            c = canvas.Canvas(pdf_file, pagesize=(width, height))
            c.drawImage(jpg_file, 0, 0, width, height)
            c.save()
            page2_instance.add_conversion_history("JPG to PDF", pdf_file)
            messagebox.showinfo("Conversion Complete", f"JPG converted to PDF: {pdf_file}")

    convert_button6 = Button(create_window, text="JPG to PDF", command=jpg_to_pdf, width=12, height=3, font=("Bold", 15), bg='#ccccff', fg='white')
    convert_button6.place(x=550, y=200)
    
   
    create_window.mainloop()


    

# login page function
def login():
    user_name = user.get()
    password = user1.get()

    if user_name == 'Username' and password == 'Password':
        messagebox.showerror('Login', "Enter username and password")
    else:
        messagebox.showinfo("Login", "Login successful")
        window.destroy()
        page()

#main intialisation


if __name__ == '__main__':
    page2_instance = None  # initialize  Page2 instance
    window = Tk()
    window.title('PDF TOOLS')
    window.geometry('925x500+300+100')
    window.configure(bg='#fff')
    window.resizable(False, False)

    img = PhotoImage(file='C:\\Users\\phani_pm2rtun\\Downloads\\login.png')
    Label(window, image=img, bg='white').place(x=50, y=50)

    frame = Frame(window, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = Label(frame, text='Create Account', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    
    # all about the username and password

    
    def remove_placeholder(text):
        if len(text) > 0:
            user_placeholder.config(text='')
            user_placeholder.place_configure(x=610)
        else:
            user_placeholder.config(text='Username')
            user_placeholder.place_configure(x=500)

    def remove1_placeholder(text):
        if len(text) > 0:
            user1_placeholder.config(text='')
            user1_placeholder.place_configure(x=610)
        else:
            user1_placeholder.config(text='Password')
            user1_placeholder.place_configure(x=500)

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Verdana', 11))
    user.place(x=30, y=80)
    user.bind('<KeyRelease>', lambda e: remove_placeholder(user.get()))

    user_placeholder = Label(window, text="Username", fg="grey", font=("Bold", 11), bg="white")
    user_placeholder.place(x=500, y=150)
    user.bind('<FocusIn>', lambda e: remove_placeholder(user.get()))
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    user1 = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Verdana', 11))
    user1.place(x=30, y=150)
    user1.bind('<KeyRelease>', lambda e: remove1_placeholder(user1.get()))

    user1_placeholder = Label(window, text="Password", fg="grey", font=("Bold", 11), bg="white")
    user1_placeholder.place(x=500, y=220)
    user1.bind('<FocusIn>', lambda e: remove1_placeholder(user1.get()))
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text='Login', bg='#57a1f8', fg='white', border=0, command=login).place(x=35, y=204)

    window.mainloop()

    
