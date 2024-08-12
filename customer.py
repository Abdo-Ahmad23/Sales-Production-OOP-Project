from validation.email_validation import Email
class Customer(Email):
    customers_list=list()
    id=0
    def __init__(self,first_name='',last_name='',phone='',email='',street='',city='',state='',zip_code=''):
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
        Customer.check_if_empty(self)
        Customer.if_valid_data(self)
    def check_if_empty(self):
        ok=True
        if(self.first_name==''):
            print('First Name is required !')
            ok=False
        if(Customer.is_valid_email(self.email)==False):
            print('This Email is not valid !')
            ok=False
        if(self.phone==''):
            print('Phone is required !')
            ok=False
        return ok
    def check_if_customer_id_is_found(self,customer_id):
        for i in range(len(Customer.customers_list)):
            if customer_id==Customer.customers_list[i]['customer_id']:
                return True
        return False
    
    def if_valid_data(self):
        if(Customer.check_if_empty(self)==True):
            new_customer={
                'customer_id':Customer.id,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'phone':self.phone,
                'email':self.email,
                'street':self.street,
                'city':self.city,
                'state':self.state,
                'zip_code':self.zip_code,
            }
            Customer.customers_list.append(new_customer)
            Customer.id+=1


Customer1=Customer('first_name','last_name','phone','email@gmail.com','street','city','state','zip_code')
# print(Customer1.customers_list[0])

# print(Customer.customers)