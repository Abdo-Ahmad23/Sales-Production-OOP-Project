from manager import Manager
class Store(Manager):
    id=0
    Stores_list=list()
    def __init__(self,store_name='',address='',zip_code=None):
        self.store_id=Store.id
        self.store_name=store_name
        self.address=address
        self.zip_code=zip_code
        Store.is_any_field_is_empty(self)
    
    def is_any_field_is_empty(self):

        if self.store_name=='':
            print("store Name is required !")
            return True

        if self.address=='':
            print("store address Field is required !")
            return True

        if self.zip_code==None:
            print("Zip code is required !")
            return True
        
        Store.Stores_list.append(
            {
                'store_id':Store.id,
                'store_name':self.store_name,
                'address':self.address,
                'zip_code':self.zip_code,

            }
        )
        Store.id+=1
        return False
    def show_all_stores(self):
        for i in range(len(Store.Stores_list)):
            print(f"store id : {Store.Stores_list[i]['store_id']}")
            print(f"store name : {Store.Stores_list[i]['store_name']}")
            print(f"Store Address : {Store.Stores_list[i]['address']}")
            print(f"Zip Code  : {Store.Stores_list[i]['zip_code']}")
            print('*'*20)
    def check_if_store_id_is_found(self,store_id):
        for i in range(len(Store.Stores_list)):
            # print(i)
            if store_id==Store.Stores_list[i]['store_id']:
                return True
        return False
store1=Store('Store1','sohag',9009)
store2=Store('Store1','sohag',1234)
store1.show_all_stores()
# store1.check_if_store_id_is_found(1)
# print(store1.check_if_store_id_is_found(110))   
    
    