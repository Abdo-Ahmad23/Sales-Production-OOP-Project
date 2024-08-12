from validation.email_validation import Email
class Manager(Email):
    id=0
    managers_list=list()
    def __init__(self,f_name='',s_name='',email='',phone='',active=True):
        self.first_name=f_name
        self.last_name=s_name
        self.email=email
        self.phone=phone
        self.active=active
        Manager.is_any_field_is_empty(self)

    def check_if_manager_id_is_found(self,manager_id):
        for i in range(len(Manager.managers_list)):
            # print(i)
            if manager_id==Manager.managers_list[i]['manager_id']:
                return True
        return False
            
    
    def is_any_field_is_empty(self):

        if self.first_name=='':
            print("First name is required !")
            return True

        if self.last_name=='':
            print("Last Name Field is required !")
            return True

        if not Manager.is_valid_email(self.email):
            print('Enter a Valid Email')
            return True
        if self.phone=='':
            print("Phone id is required !")
            return True
        
        
        Manager.managers_list.append(
            {
                'manager_id':Manager.id,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'email':self.email,
                'phone':self.phone,
                'active':self.active,
            }
        )
        Manager.id+=1
        return False
    def show_all_managers(self):
        for i in range(len(Manager.managers_list)):
            print(f"manager id : {Manager.managers_list[i]['manager_id']}")
            print(f"First name : {Manager.managers_list[i]['first_name']}")
            print(f"Last name : {Manager.managers_list[i]['last_name']}")
            print(f"Email : {Manager.managers_list[i]['email']}")
            print(f"Phone : {Manager.managers_list[i]['phone']}")
            print(f"Active : {Manager.managers_list[i]['active']}")
            print('*'*20)

manager1=Manager('manager1','ali','alixeid@gmail.com','0191929292')
manager1=Manager('manager1','ali','alixeid@gmail.com','0191929292')
# print(manager1.check_if_manager_id_is_found(1))