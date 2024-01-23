from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector as myc
import sys
import re

con = myc.connect(host="localhost", user="root", password="root")
cursor = con.cursor()
user_id = 0

def connect_database():
    cursor.execute("create database if not exists BookStore")
    cursor.execute("use BookStore")
    
    cursor.execute("""create table if not exists 
    users(user_id int primary key auto_increment, name varchar(30), surname varchar(30),
    email varchar(50), password varchar(30))""")
    
    cursor.execute("""create table if not exists 
    books(book_id int primary key auto_increment, bk_name varchar(50), authour varchar(30),
    price int)""")
    
    cursor.execute("""create table if not exists
    orders(order_id int primary key auto_increment, book_id int,user_id int, units int)""")
    con.commit()
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orderls = []
        self.total_price = 0
        self.setMinimumSize(1400, 900)
        self.setMaximumSize(1400, 900)
        self.setStyleSheet("background-color: #EAFFFF")
        self.setWindowTitle("Book Store")
        self.setWindowIcon(QIcon("bookstore.ico"))
        self.name = None
        self.surname = None
        self.user_info()
        self.setup_books()

        fnamelb = QLabel(f"{self.name} {self.surname}", self)
        fnamelb.setGeometry(40, 30, 300, 40)
        fnamelb.setFont(QFont("Montserrat", 12, weight=65))


        bookslswid = QWidget(self) 
        bookslswid.setGeometry(50, 80, 1300, 700)

        self.bookslslay = QVBoxLayout(bookslswid)
        bookslswid.setLayout(self.bookslslay)

        ls = []
        for i in range(8):
            ls.append(self.place_books(i))
            self.bookslslay.addWidget(ls[-1])


        jamilb = QLabel("Jami:", self)
        jamilb.setGeometry(40, 845, 65, 40)
        jamilb.setFont(QFont("Montserrat", 12, weight=65))
        
        self.totallb = QLabel("0", self)
        self.totallb.setGeometry(120, 845, 165, 40)
        self.totallb.setFont(QFont("Montserrat", 12, weight=65))

        orderbtn = QPushButton("Buyurtma berish", self)
        orderbtn.setGeometry(1150, 845, 200, 40)
        orderbtn.setFont(QFont("Montserrat", 12, weight=65))
        orderbtn.clicked.connect(self.place_order)

        self.show()
    
    def user_info(self):
        query = """select name, surname from users where user_id = %s"""
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()
        self.name = data[0][0]
        self.surname = data[0][1]
        print(data[0][0])
    
    def isBooksEmpty(self):
        cursor.execute("select * from books")
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True
        
    def setup_books(self):
        if self.isBooksEmpty():
            return
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Atomic Habits", "James Clear", 123456)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Million dollorlik xatolar", "Pavel Annenkov", 89000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Savdogarlar Ustozi", "Yusupov Yuldosh", 35000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Diqqat", "Kel Nyuport", 60000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("O'yla va boy bo'l", "Napaleon Hill", 57000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Boy ota va Kambag'al ota", "Robert Kiyosaki", 20000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Muvaffaqiyatli kishining 7 konikmasi", "Stiven Kovi", 70000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Ilm olish sirlari", "Someone", 20000)
        cursor.execute(query, values)

        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Alpomish", "Xalq og'zaki ijodi", 100000)
        cursor.execute(query, values)
        
        query = "insert into books(bk_name, authour, price) values(%s, %s, %s)"
        values = ("Nimadur", "Kimdue", 20000)
        cursor.execute(query, values)
        
        con.commit()
        
    def place_books(self, i):
        
        cursor.execute("select book_id, bk_name, authour, price from books")
        data = cursor.fetchall()
        
        book_data = QWidget()
        
        book_data.resize(1200, 50)

        tne = QTextEdit(data[i][1], book_data)
        tne.setReadOnly(True)
        tne.setAlignment(Qt.AlignCenter)
        
        tne.setStyleSheet("border: 2px solid")
        tne.setGeometry(10, 0, 400, 50)
        
        tne1 = QLabel(data[i][2], book_data)
        tne1.setStyleSheet("border: 2px solid;")
        tne1.setAlignment(Qt.AlignCenter)
        
        tne1.setGeometry(410, 0, 300, 50)

        tne2 = QLabel(str(data[i][3]), book_data)
        tne2.setAlignment(Qt.AlignCenter)
        tne2.setStyleSheet("border: 2px solid")
        tne2.setGeometry(710, 0, 100, 50)
        
        book_id = data[i][0]  
        count_label = QLabel("0", book_data)
        count_label.setStyleSheet("border: 2px solid")
        count_label.setAlignment(Qt.AlignCenter)
        count_label.setGeometry(860, 0, 60, 50)

        plsbtn = QPushButton("+", book_data) 
        plsbtn.setStyleSheet("border: 2px solid")
        plsbtn.setGeometry(920, 0, 50, 50)
        plsbtn.clicked.connect(lambda: self.calculate(1, book_id, count_label))
        
        mnsbtn = QPushButton("-", book_data) 
        mnsbtn.setStyleSheet("border: 2px solid")
        mnsbtn.setGeometry(970, 0, 50, 50)
        mnsbtn.clicked.connect(lambda: self.calculate(-1, book_id, count_label))
        
        return book_data
    
    def calculate(self, value, book_id, count_label):
        cursor.execute("SELECT price FROM books WHERE book_id = %s", (book_id,))
        book_price = cursor.fetchone()[0]

        current_count = int(count_label.text())

        if current_count == 0 and value < 0:
            return

        new_count = max(0, current_count + value)
        count_label.setText(str(new_count))

        self.total_price += value * book_price
        self.totallb.setText(str(max(0, self.total_price)))

        if value > 0:
            self.orderls.append((book_id, value))
        elif current_count > 0:
            self.orderls.append((book_id, value))


    def place_order(self):
        if not self.orderls:
            return

        for book_id, units in self.orderls:
            if units > 0:
                query = "INSERT INTO orders (book_id, user_id, units) VALUES (%s, %s, %s)"
                values = (book_id, user_id, units)

                cursor.execute(query, values)
                con.commit()

        self.orderls = []
        self.total_price = 0
        self.totallb.setText("0")

    
            

        
            
        
class TemporaryWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(450, 700)
        self.setMaximumSize(450, 700)
        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon("bookstore.ico"))

        label = QLabel(self)
        label.setGeometry(25, 100, 400, 400)
        movie = QMovie('welcome.gif')
        movie.setScaledSize(label.size())
        label.setMovie(movie)
        movie.start()

        QTimer.singleShot(7000, self.close)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show_temporary_window()
        connect_database()
        self.main_window = None
        self.setMinimumSize(450, 700)
        self.setMaximumSize(450, 700)
        self.setStyleSheet("background-color: #EAFFFF")
        self.setWindowTitle("Book Store")
        self.setWindowIcon(QIcon("bookstore.ico"))

        self.loginlb = QLabel(self)
        self.loginlb.setGeometry(150, 150, 150, 50)
        self.loginlb.setText("Login")
        self.loginlb.setFont(QFont("Montserrat", 20, weight=65))

        self.email_error = QLabel(self)
        self.email_error.setGeometry(50, 200, 250, 50)
        self.email_error.setFont(QFont("Montserrat", 9))
        self.email_error.setStyleSheet("color: red")
        
        
        self.email_edit = QLineEdit(self)
        self.email_edit.setGeometry(50, 250, 350, 50)
        self.email_edit.setFont(QFont("Montserrat", 12))
        self.email_edit.setPlaceholderText("Email")
        self.email_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")

        self.password_edit = QLineEdit(self)
        self.password_edit.setGeometry(50, 320, 350, 50)
        self.password_edit.setFont(QFont("Montserrat", 12))
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")
        
        self.pas_error = QLabel(self)
        self.pas_error.setGeometry(50, 370, 400, 100)
        self.pas_error.setFont(QFont("Montserrat", 8))
        self.pas_error.setStyleSheet("color: red")

        self.loginbtn = QPushButton("Login", self)
        self.loginbtn.setGeometry(50, 450, 350, 45)
        self.loginbtn.setFont(QFont("Montserrat", 12))
        self.loginbtn.setStyleSheet("border-radius: 10px; background-color: #B5FFFF")
        self.loginbtn.clicked.connect(self.check_login)

        self.regbtn = QPushButton("Register", self)
        self.regbtn.setGeometry(50, 510, 350, 45)
        self.regbtn.setFont(QFont("Montserrat", 12))
        self.regbtn.setStyleSheet("border-radius: 10px; background-color: #B5FFFF")
        self.regbtn.clicked.connect(self.showRegwindow)
        

    def show_temporary_window(self):
        temporary_window = TemporaryWindow()
        temporary_window.exec_()
        
        
        
    def check_login(self):
        self.__email = self.email_edit.text().strip()
        self.__password = self.password_edit.text().strip()
        
        if len(self.__email) == 0 or len(self.__password) == 0:
            self.email_error.setText("Fields must be filled")
        
        else:
            self.email_error.setText("")
            self.check_password(self.__password)
            self.check_email(self.__email)
        
        error1 = self.email_error.text().strip()
        error2 = self.pas_error.text().strip()
        if len(error1) == 0 and len(error2) == 0:
            self.check_data()
    
    def check_data(self):
        query = "SELECT user_id FROM users WHERE email = %s AND password = %s"

        try:
            cursor.execute(query, (self.__email, self.__password))
            data = cursor.fetchall()

            if len(data) > 0:
                global user_id
                user_id = data[0][0]
                self.show_main_window()
            else:
                self.email_error.setText("User does not exist")

        except myc.Error as e:
            print(f"Error: {e}")

    def show_main_window(self):
        
        self.close()

        if self.main_window is None:
            self.main_window = MainWindow()
            self.main_window.show()


            
    def check_email(self, email):
        reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not (re.fullmatch(reg, email)):
            self.email_error.setText("invalid email")
        else:
            self.email_error.setText("")
            
    def check_password(self, password):
        
        alpha = 0
        digits = 0
        symb = 0
        
        for i in password:
            if i.isdigit():
                digits += 1
            elif i.isalpha():
                alpha += 1
            else:
                symb += 1
        
        if not (alpha >= 6 and digits >= 1 and symb >= 1):
            self.pas_error.setText("Password must contain at least six alpha characters\none digit and one symbol")
        else:
            self.pas_error.setText("")
    
    
    def showRegwindow(self):
        reg = RegistrationWindow()
        if reg.exec_() == QDialog.Accepted:
            self.show()
        else:
            self.close()
    
        

class RegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()
        connect_database()
        self.setMinimumSize(450, 700)
        self.setMaximumSize(450, 700)
        self.setStyleSheet("background-color: #EAFFFF")
        self.setWindowTitle("Book Store")
        self.setWindowIcon(QIcon("bookstore.ico"))

        self.namelb = QLabel(self)
        self.namelb.setGeometry(50, 50, 300, 40)
        self.namelb.setFont(QFont("Montserrat", 10))
        self.namelb.setStyleSheet("color:red")

        self.name_edit = QLineEdit(self)
        self.name_edit.setGeometry(50, 90, 350, 50)
        self.name_edit.setFont(QFont("Montserrat", 12))
        self.name_edit.setPlaceholderText("Name")
        self.name_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")

        self.surnamelb = QLabel(self)
        self.surnamelb.setGeometry(50, 140, 320, 40)
        self.surnamelb.setFont(QFont("Montserrat", 10))
        self.surnamelb.setStyleSheet("color:red")
        
        self.surname_edit = QLineEdit(self)
        self.surname_edit.setGeometry(50, 190, 350, 50)
        self.surname_edit.setFont(QFont("Montserrat", 12))
        self.surname_edit.setPlaceholderText("Surname")
        self.surname_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")
        
        self.emaillb = QLabel(self)
        self.emaillb.setGeometry(50, 240, 200, 40)
        self.emaillb.setFont(QFont("Montserrat", 10))
        self.emaillb.setStyleSheet("color:red")

        self.email_edit = QLineEdit(self)
        self.email_edit.setGeometry(50, 290, 350, 50)
        self.email_edit.setFont(QFont("Montserrat", 12))
        self.email_edit.setPlaceholderText("Email")
        self.email_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")

        self.passwordlb = QLabel(self)
        self.passwordlb.setGeometry(50, 340, 350, 40)
        self.passwordlb.setFont(QFont("Montserrat", 10))
        self.passwordlb.setStyleSheet("color:red")
        
        self.password_edit = QLineEdit(self)
        self.password_edit.setGeometry(50, 390, 350, 50)
        self.password_edit.setFont(QFont("Montserrat", 12))
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")

        self.repasswordlb = QLabel(self)
        self.repasswordlb.setGeometry(50, 440, 250, 40)
        self.repasswordlb.setFont(QFont("Montserrat", 10))
        self.repasswordlb.setStyleSheet("color:red")
        
        self.repassword_edit = QLineEdit(self)
        self.repassword_edit.setGeometry(50, 480, 350, 50)
        self.repassword_edit.setFont(QFont("Montserrat", 12))
        self.repassword_edit.setPlaceholderText("Re-enter Password")
        self.repassword_edit.setStyleSheet("border: 1px solid #00FFFF; border-radius: 10px")

        register_button = QPushButton("Register", self)
        register_button.setGeometry(50, 560, 350, 45)
        register_button.setFont(QFont("Montserrat", 12))
        register_button.setStyleSheet("border-radius: 10px; background-color: #B5FFFF")
        register_button.clicked.connect(self.register_button_clicked)

    def register_button_clicked(self):
        
        registration_successful = self.check_info()

        if registration_successful:
            self.accept()  # Set the result to QDialog.Accepted
            
    def check_info(self):
        
        self.__name = self.name_edit.text().strip()
        self.__surname = self.surname_edit.text().strip()
        self.__email = self.email_edit.text().strip()
        self.__password = self.password_edit.text().strip()
        self.__repassword = self.repassword_edit.text().strip()
        isValid = 1
        
        if len(self.__name) < 3:
            self.namelb.setText("Name cannot be that much short")
            isValid = 0
        
        if len(self.__surname) < 3:
            self.surnamelb.setText("Surname cannot be that much short")
            isValid = 0
        
        reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not (re.fullmatch(reg, self.__email)):
            self.emaillb.setText("Invalid email address")
            isValid = 0
        
        if self.check_password(self.__password):
            isValid = 0
        
        if not self.check_password(self.__password) and self.__password != self.__repassword:
            self.repasswordlb.setText("Password does not match")
            isValid = 0
        
        if isValid:
            if self.check_data():
                self.emaillb.setText("User already exists")
                QTimer.singleShot(5000, self.accept)
                return 0
            
            self.write_data()
            return True
        
        else:
            return False
    
    def check_data(self):
        query = "SELECT user_id FROM users WHERE email = %s"

        try:
            cursor.execute(query, (self.__email,))
            data = cursor.fetchall()
            
            if len(data) > 0:
                return 1
            else:
                return 0

        except myc.Error as e:
            print(f"Error: {e}")
        
    def check_password(self, password):
        
        alpha = 0
        digits = 0
        symb = 0
        
        for i in password:
            if i.isdigit():
                digits += 1
            elif i.isalpha():
                alpha += 1
            else:
                symb += 1
        
        if not (alpha >= 6 and digits >= 1 and symb >= 1):
            self.passwordlb.setText("Password must contain at least six alpha characters\none digit and one symbol")
            return 1
        else:
            return 0
    
    def write_data(self):
        
        query = f"""insert into users(name, surname, email, password) values(%s, %s, %s, %s)"""
        values = (self.__name, self.__surname, self.__email, self.__password)
        cursor.execute(query, values)
        con.commit()
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = LoginWindow()
    win.show()

    sys.exit(app.exec_())

