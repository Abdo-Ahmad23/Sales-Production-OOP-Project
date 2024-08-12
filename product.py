from category import Category
from brand import Brand
class Product(Category,Brand):

    id=0
    Products_list=list()
    def __init__(self,product_name='',brand_id=None,category_id=None,price=None,model_year=None):
        self.product_id=Product.id
        self.product_name=product_name
        self.brand_id=brand_id
        self.category_id=category_id
        self.model_year=model_year
        self.product_price=price
        Product.is_any_field_is_empty(self)
    

    def check_if_product_id_is_found(self,product_id):
        for i in range(len(Product.Products_list)):
            # print(i)
            if product_id==Product.Products_list[i]['product_id']:
                return True
        return False


    def check_is_found(self):
        if not Category.check_if_category_id_is_found(self,self.category_id):
            print('This Category id is not found !')
            return False
        if not Brand.check_if_brand_id_is_found(self,self.brand_id):
            print('This brand id is not found !')
            return False
        return True


    def is_any_field_is_empty(self):

        if self.product_name=='':
            print("Product id is required !")
            return True

        if self.product_price==None:
            print("Product Price Field is required !")
            return True

        if self.brand_id==None:
            print("Brand id is required !")
            return True
        if self.category_id==None:
            print("Category id is required !")
            return True
        if not Product.check_is_found(self):
            # Product.check_is_found(self)
            # print('k')
            return True
        Product.Products_list.append(
            {
                'product_id':Product.id,
                'product_name':self.product_name,
                'brand_id':self.brand_id,
                'category_id':self.category_id,
                'model_year':self.model_year,
                'product_price':self.product_price,

            }
        )
        Product.id+=1
        return False
    def show_all_products(self):
        for i in range(len(Product.Products_list)):
            print(f"Product id : {Product.Products_list[i]['product_id']}")
            print(f"Product name : {Product.Products_list[i]['product_name']}")
            print(f"Brand id : {Product.Products_list[i]['brand_id']}")
            print(f"Category id : {Product.Products_list[i]['category_id']}")
            print(f"Model year : {Product.Products_list[i]['model_year']}")
            print(f"Product price : {Product.Products_list[i]['product_price']}")
            print('*'*20)
   

product1=Product('proudct1',0,0,900)
# product2=Product('proudct2',1,1,900)
# product1.show_all_products()
# print(Product.Products_list)

        