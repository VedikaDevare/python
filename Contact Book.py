contact=[]
def add_contact():
    n=int(input("Enter number contact do you want to add:"))
    for i in range(1,n+1):
        add = input("Add your contact:")
        contact.append(add)
    print("Contact is added to your book.")
def view_contact():
    for person in contact:
        print(person)
def search_contact():
    search = input("Enter contact to search:")
    if search in contact:
        print("Contact found.")
    else:
        print("Contact not found.")
def delete_contact():
    delete = input("Enter contact to delete:")
    if delete in contact:
        contact.remove(delete)
        print("Contact is Deleted")
    else:
        print("Contact is not found.")
print("---MENU---")
print("1.Add Contact.\n2.View Contact.\n3.Searh Contact.\n4.Delete Contact.\n5.Exit.")
while True:
    choice=int(input("Select Your choice:"))
    if choice==1:
        add_contact()
    if choice==2:
        view_contact()
    if choice==3:
        search_contact()
    if choice==4:
        delete_contact()
    if choice==5:
        print("You are out of the program.")