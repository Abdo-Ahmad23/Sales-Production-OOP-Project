from store import Store
from product import Product
class Stock(Store,Product):
    id=0
    Stocks_list=list()
    def __init__(self,store_id=None,product_id=None,quantity=None):
        self.store_id=store_id
        self.product_id=product_id
        self.quantity=quantity
        Stock.check_if_error_in_inputs(self)

    def check_if_not_found(self):
        if not Store.check_if_store_id_is_found(self,self.store_id):
            print('This store id is not found')
        if not Product.check_if_product_id_is_found(self,self.product_id):
            print('This Product id is not found')

    def check_if_error_in_inputs(self):
        if self.store_id==None:
            print('store id field is required')
            return True
        if self.product_id==None:
            print('Product id field is required')
            return True
        if self.quantity==None:
            print('Quantity field is required')
            return True
        if Stock.check_if_not_found(self):
            return True

        Stock.Stocks_list.append(
            {
                'stock_id':Stock.id,
                'store_id':self.store_id,
                'product_id':self.product_id,
                'quantity':self.quantity,
            }
        )
        Stock.id+=1
        return False
    def show_all_stocks(self):
        for i in range(len(Stock.Stocks_list)):
                print(f"stock id : {Stock.Stocks_list[i]['stock_id']}")
                print(f"store id : {Stock.Stocks_list[i]['store_id']}")
                print(f"product id : {Stock.Stocks_list[i]['product_id']}")
                print(f"quantity : {Stock.Stocks_list[i]['quantity']}")
                print('*'*20)
        
    
# stock1=Stock(0,0,11)
stock1=Stock(110,0,11)
# stock1.show_all_stocks()
# print(Stock.id)
