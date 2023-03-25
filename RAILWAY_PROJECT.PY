import mysql.connector
railway_project = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "railway_project"
)

# print(railway_project)

railway_data = railway_project.cursor()

# railway_data.execute("CREATE DATABASE RAILWAY_PROJECT")

# railway_data.execute("CREATE TABLE TRAIN (NAME VARCHAR(50), COST INT, DISTANCE INT, DATE VARCHAR(50))")

# railway_data.execute("CREATE TABLE CUSTOMER (NAME VARCHAR(50), TRAIN VARCHAR(50), PAYMENT INT, DATE VARCHAR(50), PHONE VARCHAR(50))")

# railway_data.execute("CREATE TABLE BILLS (DETAILS VARCHAR(50), COST INT, DATE VARCHAR(50))")

# railway_data.execute("CREATE TABLE WORKER (NAME VARCHAR(100), WORK VARCHAR(100), SALARY VARCHAR(100)) ")


# railway_project.commit()


##################################### Programming ########################################

def AddTrain():
    n = input("Train Name: ")
    c = input("Cost: ")
    b = input("Distance: ")
    d = input("Date: ")
    data = (n,c,b,d)
    sql = "INSERT INTO TRAIN values (%s,%s,%s,%s)"
    railway_data = railway_project.cursor()
    railway_data.execute(sql,data)
    railway_project.commit()
    print("\nData Inserted Sucessfully")
    main()

def DisplayTrain():
    sql = 'SELECT * FROM Train'
    railway_data = railway_project.cursor()
    railway_data.execute(sql)
    x = railway_data.fetchall()
    for i in x:
        print("Name: ",i[0])
        print("Cost: ",i[1])
        print("Distance: ",i[2])
        print("Date: ",i[3])
        print(".......................................................")
    main()

def BookTrain():
    n = input("Customer Name: ")
    s = input("Train: ")
    py = int(input("Payment: "))
    d = input("Date: ")
    p = input("Phone: ")
    data = (n,s,py,d,p)
    sql = "INSERT INTO CUSTOMER values(%s,%s,%s,%s,%s)"
    railway_data = railway_project.cursor()
    railway_data.execute(sql,data)
    railway_project.commit()
    print("\nData Inserted Sucessfully")
    main()

def DisplayPayments():
    sd = input("Date: ")
    sql = "SELECT * FROM CUSTOMER"
    railway_data = railway_project.cursor()
    railway_data.execute(sql)
    x = railway_data.fetchall()
    for i in x:
        if i[3] == sd:
            print("Name:",i[0])
            print("Train:",i[1])
            print("Payment:",i[2])
            print("Date:",i[3])
            print("Phone:",i[4])
            print(".........................................................")
        main()

def AddBill():
    dt = input("Details: ")
    c = input("Cost: ")
    d = input("Date: ")
    data = (dt,c,d)
    sql = "INSERT INTO BILLS values(%s,%s,%s)"
    railway_data = railway_project.cursor()
    railway_data.execute(sql,data)
    railway_project.commit()
    print("\nData Inserted Sucessfully")
    main()

def DisplayBills():
    sd = input("Date: ")
    sql = "SELECT * FROM BILLS"
    railway_data = railway_project.cursor()
    railway_data.execute(sql)
    x = railway_data.fetchall()
    for i in x:
        if i[2] == sd:
            print("Detail:",i[0])
            print("Cost:",i[1])
            print("Date:",i[2])
            print("............................................................")
        main()

def AddWorker():
    n = input("Name: ")
    w = input("Work: ")
    s = input("Salary: ")
    data = (n,w,s)
    sql = "INSERT INTO WORKER values(%s,%s,%s)"
    railway_data = railway_project.cursor()
    railway_data.execute(sql,data)
    railway_project.commit()
    print("\nData Inserted Sucessfully")
    main()

def DisplayWorkers():
    sql = "SELECT * FROM WORKER"
    railway_data = railway_project.cursor()
    railway_data.execute(sql)
    x = railway_data.fetchall()
    for i in x:
        print("Name:",i[0])
        print("Work:",i[1])
        print("Salary:",i[2])
        print(".....................................................")
    main()



def main():
    print("""
    
    1. Add Train
    2. Book Train
    3. Add Bill
    4. Add Worker
    5. Display Train
    6. Display Payments
    7. Display Bills
    8. Display Workers
    
    """)

    choice = input("Select Option: ")
    while True:
        if(choice == '1'):
            AddTrain()
        elif(choice == '2'):
            BookTrain()
        elif(choice == '3'):
            AddBill()
        elif(choice == '4'):
            AddWorker()
        elif(choice == '5'):
            DisplayTrain()
        elif(choice == '6'):
            DisplayPayments()
        elif(choice == '7'):
            DisplayBills()
        elif(choice == '8'):
            DisplayWorkers()
        else:
            print("Enter Again.....")
        main()


def pswd():
        print(" ---------------------------->>>>>Welcome Railway System<<<<<<---------------------")
        print("\n")
        id = input("Enter your id: ")
        ps = input("Enter password: ")
        if id == "chandu":
            main()
        elif ps == "123":
            main()
        else:
            print("Invalid....")
            pswd()
pswd()






      

