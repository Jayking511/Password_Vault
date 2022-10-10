import sys
import pyfiglet
import Master_Password_Hash_Check
import database_connect
import getpass
import tabulate


def main():
    for i in range(3):
        master_password=getpass.getpass("Enter your Master Password : ")
        if Master_Password_Hash_Check.isPassword(master_password):
            create_database()
            print("\nWelcome to your Vault :)")
            print("Use help command for available options.\n")
            while True:
                option=input("[?] Select an option :")
                if option=='0':
                    print("GoodBye!")
                    break
                elif option=='1':
                    list_websites()
                    continue
                elif option=='2':
                    view_all_passwords()
                    continue
                elif option=='3':
                    view_password()
                    continue
                elif option=='4':
                    create_password()
                    continue
                elif option=='5':
                    delete_password()
                    continue
                elif option=='6':
                    update_password()
                    continue
                elif option=='help':
                    print("\n[0] exit")
                    print("[1] List all websites")
                    print("[2] View all passwords")
                    print("[3] View Password")
                    print("[4] Create Password")
                    print("[5] Delete Password")
                    print("[6] Update Password\n")
                else:
                    print("Please enter a valid option")
                    continue
            break
        else:
            if i!=2:
                print("Please check the password and try again")
            else:
                print("Incorrect password attempted multiple times.")
                print("Terminating connection to Vault.\nTry again later.")
    return


def create_database():
    statement="create database"
    database_connect.mysql_statement(statement)
    return


def list_websites():
    print()
    statement="select attribute from table_name"
    result=database_connect.mysql_statement(statement)
    for i in result:
        print(i)
    print()
    return


def view_all_passwords():
    statement="select * from table_name"
    result=database_connect.mysql_statement(statement)
    l=[]
    tablelist=[]
    for i,attr in enumerate(result):
        if (i+1)%3!=0:
            l.append(attr)
        else:
            l.append(attr)
            tablelist.append(l)
            l=[]
    table=tabulate.tabulate(tablelist, headers=['Website', 'Username', 'Password'])
    print(table)
    return


def view_password():
    website=input("Website: ")
    valid=database_connect.mysql_statement("select attribute from table_name")
    if website not in valid:
        print(f"Password for {website} is not stored.\nTry again.")
        return
    statement=f"select * from table_name where attribute = '{website}'"
    result=database_connect.mysql_statement(statement)
    for i,attr in enumerate(result):
        if i==0:
            print(f"\nWebsite  : {attr}")
        if i==1:
            print(f"Username : {attr}")
        if i==2:
            print(f"Password : {attr}\n")
    return


def create_password():
    website = input("Website: ")
    if website=="":
        print("Website name cannot be empty.")
        return
    valid=database_connect.mysql_statement("select attribute from table_name")
    if website in valid:
        print(f"Password for {website} is already stored.\nTry again.")
        return
    username = input("Username: ")
    password1 = input("Password: ")
    password2 = input("Enter the Password again: ")
    if password1==password2:
        statement=f"insert into table_name values ('{website}', '{username}', '{password1}')"
        database_connect.mysql_statement(statement)
        print(f"Password for {website} created successfully :)")
    else:
        print("Passwords not matched.\nTry again.")
    return


def delete_password():
    website=input("Website: ")
    valid=database_connect.mysql_statement("select attribute from table_name")
    if website not in valid:
        print(f"Password for {website} is not stored.\nTry again.")
        return
    statement=f"delete from table_name where attribute = '{website}'"
    database_connect.mysql_statement(statement)
    print(f"Password for {website} deleted successfully :)")
    return


def update_password():
    website = input("Website: ")
    valid=database_connect.mysql_statement("select attribute from table_name")
    if website not in valid:
        print(f"Password for {website} is not stored.\nTry again.")
        return
    username = input("Username: ")
    password1 = input("New Password: ")
    password2 = input("Enter the Password again: ")
    if password1==password2:
        statement=f"delete from table_name where attribute = '{website}'"
        database_connect.mysql_statement(statement)
        statement=f"insert into table_name values ('{website}', '{username}', '{password1}')"
        database_connect.mysql_statement(statement)
        print(f"Password for {website} updated successfully :)")
    else:
        print("Passwords not matched.\nTry again.")
    return


print(pyfiglet.figlet_format("Password Vault", font="slant"))
print("Manage all passwords at one place")
print("[0] Exit")
print("[1] Enter\n")
choice = input("[?] Enter your choice : ")

if choice=='0':
    print("GoodBye!")
    sys.exit()
elif choice=='1':
    main()
else:
    print('Please enter a valid option')
    sys.exit()
