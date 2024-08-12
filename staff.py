from validation.email_validation import Email
from store import Store
from manager import Manager
class Staff(Store,Manager,Email):
    id=0
    Staff_list=list()
    def __init__(self,first_name='',last_name='',email='',phone='',active=True,store_id=None,manager_id=None):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.active=active
        self.store_id=store_id
        self.manager_id=manager_id
        Staff.is_any_field_is_empty(self)
        
    def check_is_found(self):
        if not Store.check_if_store_id_is_found(self,self.store_id):
            print('This store id is not found !')
            return False
        elif not Manager.check_if_manager_id_is_found(self,self.manager_id):
            print('This Manager id is not found !')
            return False
        else:
            # print("blablabla")
            return True
    def is_any_field_is_empty(self):

        if self.first_name=='':
            print("First name is required !")
            return True

        if self.last_name=='':
            print("Last Name Field is required !")
            return True

        if not Staff.is_valid_email(self.email):
            print('Enter a Valid Email')
            return True
        if self.phone=='':
            print("Phone id is required !")
            return True
        if self.store_id==None:
            print("Store id is required !")
            return True
        if self.manager_id==None:
            print("Manager id is required !")
            return True
        if not Staff.check_is_found(self):
            # Staff.check_is_found(self)
            return True
        Staff.Staff_list.append(
            {
                'staff_id':Staff.id,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'email':self.email,
                'phone':self.phone,
                'active':self.active,
                'manager_id':self.manager_id,
            }
        )
        Staff.id+=1
        return False

    def check_if_staff_id_is_found(self,staff_id):
        for i in range(len(Staff.Staff_list)):
            if staff_id==Staff.Staff_list[i]['staff_id']:
                return True
        return False
    
    def show_all_staffs(self):
        for i in range(len(Staff.Staff_list)):
            print(f"Staff id : {Staff.Staff_list[i]['staff_id']}")
            print(f"First name : {Staff.Staff_list[i]['first_name']}")
            print(f"Last name : {Staff.Staff_list[i]['last_name']}")
            print(f"Email : {Staff.Staff_list[i]['email']}")
            print(f"Phone : {Staff.Staff_list[i]['phone']}")
            print(f"Active : {Staff.Staff_list[i]['active']}")
            print(f"Manager id : {Staff.Staff_list[i]['manager_id']}")
            print('*'*20)
    
stuff1=Staff('Ali','Nasser','alixeid@gmail.com','01234567890',True,1,1)

# stuff1.show_all_staffs()

# print(stuff1.Staff_list)
# stuff1.check_is_found()