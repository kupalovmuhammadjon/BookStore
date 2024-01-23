class BookWidget(QWidget):
    def __init__(self, data):
        super().__init__()

        tne = QTextEdit(data[0], self)
        tne.setReadOnly(True)
        tne.setAlignment(Qt.AlignCenter)
        tne.setStyleSheet("border: 2px solid")
        tne.setGeometry(10, 0, 400, 50)

        tne1 = QLabel(data[1], self)
        tne1.setStyleSheet("border: 2px solid;")
        tne1.setAlignment(Qt.AlignCenter)
        tne1.setGeometry(410, 0, 400, 50)

        tne2 = QLabel(str(data[2]), self)
        tne2.setAlignment(Qt.AlignCenter)
        tne2.setStyleSheet("border: 2px solid")
        tne2.setGeometry(810, 0, 190, 50)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1400, 900)
        self.setMaximumSize(1400, 900)
        self.setStyleSheet("background-color: #EAFFFF")
        self.setWindowTitle("Book Store")
        self.setWindowIcon(QIcon("bookstore.ico"))

        self.name = None
        self.surname = None
        self.setup_books()

        fnamelb = QLabel(f"{self.name} {self.surname}", self)
        fnamelb.setGeometry(40, 30, 300, 40)
        fnamelb.setFont(QFont("Montserrat", 12, weight=65))

        bookslswid_layout = QFormLayout()
        bookslswid = QGroupBox("Books")
        bookslswid.setLayout(bookslswid_layout)
        booksls = QScrollArea()
        booksls.setWidget(bookslswid)
        booksls.setWidgetResizable(True)
        booksls.setFixedHeight(400)

        for i in range(10):
            book_widget = BookWidget(self.get_book_data(i))
            bookslswid_layout.addRow(book_widget)

        jamilb = QLabel("Jami:", self)
        jamilb.setGeometry(40, 845, 65, 40)
        jamilb.setFont(QFont("Montserrat", 12, weight=65))

        orderbtn = QPushButton("Buyurtma berish", self)
        orderbtn.setGeometry(1150, 845, 200, 40)
        orderbtn.setFont(QFont("Montserrat", 12, weight=65))

        central_layout = QVBoxLayout(self)  # Create a layout for the central widget
        central_layout.addWidget(booksls)  # Add the scroll area to the central layout
        self.setCentralWidget(QWidget())  # Set a central widget (an empty one for layout purposes)

        self.show()

    def get_book_data(self, i):
        cursor.execute("select bk_name, authour, price from books")
        data = cursor.fetchall()
        return data[i]
    
    def user_info(self):
        query = """select name, surname from users where user_id = %s"""
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()
        self.name = data[0][0]
        self.surname = data[0][1]
    
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
        cursor.execute("select bk_name, authour, price from books")
        data = cursor.fetchall()

        book_data = QWidget()

        book_data.resize(1200, 50)

        tne = QLabel(data[i][0], book_data)
        tne.setAlignment(Qt.AlignCenter)
        tne.setStyleSheet("border: 2px solid")
        tne.setGeometry(10, 0, 400, 50)

        tne1 = QLabel(data[i][1], book_data)
        tne1.setStyleSheet("border: 2px solid;")
        tne1.setAlignment(Qt.AlignCenter)
        tne1.setGeometry(410, 0, 400, 50)

        tne2 = QLabel(str(data[i][2]), book_data)
        tne2.setAlignment(Qt.AlignCenter)
        tne2.setStyleSheet("border: 2px solid")

        tne2.setGeometry(810, 0, 190, 50)

        return book_data
