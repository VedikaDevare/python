contact={}
def add_contact():
    n=int(input("Enter number of contacts do you want to add:"))
    for i in range(1,n+1):
        key= input("Enter name:")
        value= input("Enter number:")
        contact.update({key:value})
    print("Contact is added to your book.")
def view_contact():
    for name, number in contact.items():
        print(name, ":", number)
def search_contact():
    search = input("Enter contact to search:")
    if search in contact:
        print(contact.get(search))
    else:
        print("Contact not found.")
def delete_contact():
    delete = input("Enter contact to delete:")
    if delete in contact:
        contact.pop(delete)
        print("Contact is Deleted")
    else:
        print("Contact is not found.")
def update_contact():
    up=input("Enter contact to update:")
    if up in contact:
        update=input("Enter updated number:")
        contact[up]= update 
        print("Number is Updated.")
    else:
        print("No contact found.")
print("---MENU---")
print("1.Add Contact.\n2.View Contact.\n3.Searh Contact.\n4.Delete Contact.\n5.Update Contact\n6.Exit.")
while True:
    choice=int(input("Select Your choice:"))
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        delete_contact()
    elif choice==5:
        update_contact()
    elif choice==6:
        print("Thank you for using contact book.")
        break