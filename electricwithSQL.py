import mysql.connector

def connectDB():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kenthlangnamankasitoe27321",
        database="electric_company"
    )

class customersDC:
    def __init__(self):
        self.customerNAME = ""
        self.classiFICT = ""
        self.totalKWU = 0.0
        self.ratePKU = 0.0
        self.groAMT = 0.0
        self.misceCHAR = 0.0
        self.totalAMT = 0.0
        self.prevREADING = 0.0
        self.currREADING = 0.0
        self.meterID = 0

def main():
    while True:
        print("\n[ELECTRIC COMPANY]")
        print("1. Calculate Bill")
        print("2. Visit Database")
        print("3. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            choice = -1
        match choice:
            case 1:
                elecCAL()
            case 2:
                dataBASE()
            case 3:
                exit()
                return
            case _:
                for i in range(3):
                    print("\n[PLEASE ENTER A VALID INPUT]")

def elecCAL():
    customers = customersDC()
    print("\n[CALCULATE ELECTRIC BILL]")
    customers.customerNAME = input("Enter Customer Name: ")
    customers.meterID = int(input("\nEnter Meter ID: "))
    customers.classiFICT = input("\nEnter Classification: ")
    customers.prevREADING = float(input("\nEnter Previous Reading: "))
    customers.currREADING = float(input("\nEnter Current Reading: "))
    # BRUHH
    customers.totalKWU = customers.currREADING - customers.prevREADING
    if customers.classiFICT.lower() == "residential":
        if customers.totalKWU > 300:
            customers.misceCHAR = 0.8
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)
        elif customers.totalKWU >= 100 and customers.totalKWU <= 299:
            customers.misceCHAR = 0.5
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)
        elif customers.totalPKU < 100:
            customers.misceCHAR = 0
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)
    elif customers.classiFICT.lower() == "commercial":
        if customers.totalKWU > 300:
            customers.misceCHAR = 0.8
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)
        elif customers.totalKWU >= 100 and customers.totalKWU <= 299:
            customers.misceCHAR = 0.5
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)
        elif customers.totalKWU < 100:
            customers.misceCHAR = 0
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            saveDB(customers)
            disPLAY(customers)

def dataBASE():
    db = connectDB()
    cursor = db.cursor()
    cursor.execute("SELECT customer_name, meter_id, total_amount FROM customers")
    records = cursor.fetchall()
    print("\n[CUSTOMERS' DATABASE]")
    for record in records:
        print(f"CUSTOMER NAME: {record[0]} || METER ID: {record[1]} || TOTAL AMOUNT DUE: {record[2]}")
    
    db.close()

def disPLAY(customers):
    print(f"Customer Name: {customers.customerNAME}")
    print(f"Total Kilowatt Usage: {customers.totalKWU:.2f} kWh")
    print(f"Rate Per Kilowatt: {customers.ratePKU:.2f} kWh")
    print(f"Gross Amount: {customers.groAMT:.2f} PHP")
    print(f"Miscellaneous Charges: {customers.misceCHAR:.2f} PHP")
    print(f"Total Amount Due: {customers.totalAMT:.2f} PHP")

def exit():
    print("\n[THANK YOU FOR USING!]")

def saveDB(customers):
    db = connectDB()
    cursor = db.cursor()
    query = """INSERT INTO customers(customer_name, meter_id, classification, total_kw_usage, rate_per_kw_usage, gross_amt, misce_charges, total_amount, previous_reading, current_reading)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        customers.customerNAME, customers.meterID, customers.classiFICT, customers.totalKWU,
        customers.ratePKU, customers.groAMT, customers.misceCHAR, customers.totalAMT,
        customers.prevREADING, customers.currREADING
    )
    # some finalization :D
    cursor.execute(query, values)
    db.commit()
    db.close()
    print("\n[DATA SAVED]")

if __name__ == "__main__":
    main()