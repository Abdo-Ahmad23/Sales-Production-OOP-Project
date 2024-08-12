from customer import Customer
from store import Store
from staff import Staff
from validation.email_validation import Email
class Order(Staff,Store,Customer):
    id=0
    Orders_list=list()
    # itemId=0
    def __init__(self,customer_id=None,order_status='',order_date='',required_date='',shipped_date='',store_id=None,staff_id=None):
        self.customer_id=customer_id
        self.order_status=order_status
        self.order_date=order_date
        self.required_date=required_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id
        Order.is_any_field_is_empty(self)
    def check_is_found(self):
        if not Store.check_if_store_id_is_found(self,self.store_id):
            print('This Store id is not found !')
            return False
            
        if not Staff.check_if_staff_id_is_found(self,self.staff_id):
            print('This staff id is not found !')
            return False

        elif not Customer.check_if_customer_id_is_found(self,self.customer_id):
            print('This customer id is not found !')
            return False
        else:
            return True
            
    
    def is_any_field_is_empty(self):

       
        if not Order.check_is_found(self):
            # Customer.check_is_found(self)
            # print('k')
            return True
        Order.Orders_list.append(
            {
                'order_id':Order.id,
                'customer_id':self.customer_id,
                'order_status':self.order_status,
                'order_date':self.order_date,
                'required_date':self.required_date,
                'shipped_date':self.shipped_date,
                'store_id':self.store_id,
                'staff_id':self.staff_id,

            }
        )
        Order.id+=1
        return False
    def show_all_orders(self):
        for i in range(len(Order.Orders_list)):
            print(f"Order id : {Order.Orders_list[i]['order_id']}")
            print(f"Customer id : {Order.Orders_list[i]['customer_id']}")
            print(f"order status : {Order.Orders_list[i]['order_status']}")
            print(f"order date : {Order.Orders_list[i]['order_date']}")
            print(f"required date : {Order.Orders_list[i]['required_date']}")
            print(f"shipped date : {Order.Orders_list[i]['shipped_date']}")
            print(f"store id : {Order.Orders_list[i]['store_id']}")
            print(f"staff id : {Order.Orders_list[i]['staff_id']}")
            print('*'*20)
   
order=Order(0,True,'19/9/2023','20/9/2023','19/9/2023',0,0)
order=Order(0,True,'19/9/2023','20/9/2023','19/9/2023',0,0)
# order.show_all_orders()
# print(order.Orders_list)
