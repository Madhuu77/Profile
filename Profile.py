"""
Created on Fri Apr 26 12:30:18 2024

@author: Madhu
"""
class Customer:
    def __init__(self, name, ph_no, email):
        self.name = [name]
        self.email = [email]
        self.ph_no = [ph_no]

    def Add(self, name, ph_no, email):
        if name not in self.name:
            self.name.append(name)
        if ph_no not in self.ph_no:
            self.ph_no.append(ph_no)
        if email not in self.email:
            self.email.append(email)

    def Update_Name(self, old_name, new_name):
        if old_name in self.name:
            index = self.name.index(old_name)
            self.name[index] = new_name

    def Update_ph_no(self, old_ph, new_ph):
        if old_ph in self.ph_no:
            index = self.ph_no.index(old_ph)
            self.ph_no[index] = new_ph

    def Update_email(self, old_mail, new_mail):
        if old_mail in self.email:
            index = self.email.index(old_mail)
            self.email[index] = new_mail

    def display(self):
        print("Name:", self.name, "\n")
        print("Phone no.:", self.ph_no, "\n")
        print("E-mail address:", self.email, "\n")

print("\nCustomer details before update.\n")
customer = Customer("Madhu", "8618112973", "v8000m@gmail.com")
customer.display()
print("\nCustomer details After update.\n")
customer.Update_Name("Madhu", "Madhu.v")
customer.Update_ph_no("8618112973", "9341374162")
customer.Update_email("v8000m@gmail.com", "madhu8000m@gmail.com")
customer.display()
