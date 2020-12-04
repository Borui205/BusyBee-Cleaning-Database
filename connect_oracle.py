import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "C:\\Users\\Heather\\AppData\\Local\\Programs\\Python\\Python39\\instantclient_19_9")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on **************.edu

dsnStr = cx_Oracle.makedsn("-the miami edu website-", "-the SID-", "CSC423")

connection = cx_Oracle.connect(
    user="************", password="*********", dsn=dsnStr)
cursor = connection.cursor()

def theGetter():
    # get column names from cursor
    columns = [c[0] for c in cursor.description]
    # fetch data
    data = cursor.fetchall()
    # bring data into a pandas datafram for easy data transformation
    df = pd.DataFrame(data, columns = columns)
    print(df) #examine
    print(df.columns)
    # print(df['FIRST_NAME']) # example to extract a column

def switch():
    print("HI! WELCOME TO THE BUSYBEE CLEANING COMPANY MENU. PICK FROM THE FOLLOWING QUERIES:")
    print("1: Requirements for the Cardboard Box Company?")
    print("2: Clients that Maria Lopez Services?")
    print("3: Average salary at the BusyBee Cleaning Company?")
    print("4: Equipment that Costs equal to or greater than 3000?")
    print("5: Clients located in Coral Gables?")

    option = int(input(" YOUR OPTION: "))
    
    def opOne():
        cursor.execute("""SELECT c.fname, r.staffNo, r.equipID, r.startTime, r.endTime, r.daysOfWeek 
        FROM Client c, Requirements r 
        WHERE c.clientNo = r.clientNo AND c.clientNo = 'CL001'""")
        theGetter()

    def opTwo():
        cursor.execute("""SELECT c.clientNo, c.fname, c.lname
        FROM Client c, Requirements r
        WHERE c.clientNo=r.clientNo AND r.staffNo = 'SF001'
        GROUP BY c.clientNo, c.fname, c.lname""")
        theGetter()
    
    def opThree():
        cursor.execute("SELECT AVG(Salary) AS AverageSalary FROM Employees")
        theGetter()
    
    def opFour():
        cursor.execute("""SELECT EquipID, equipDesc, equipCost
        FROM Equipment
        WHERE equipCost >= 3000
        """)
        theGetter()
    
    def opFive():
        cursor.execute("""SELECT clientNo, fname, lname, address
        FROM Client
        WHERE address LIKE '%CORAL GABLES%'
        """)
        theGetter()
    
    def opSix():
        print("Quitting program")
        quit()
    
    def default():
        print("Try again picking 1-5 or press 6 to exit...")
        
    
    dict = {
        1 : opOne,
        2 : opTwo,
        3 : opThree,
        4 : opFour,
        5 : opFive,
        6 : opSix,
    }
    dict.get(option,default)()

    if (option != 6):
        switch()
       
    

switch()

