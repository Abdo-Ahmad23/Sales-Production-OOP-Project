class Brand:
    Brands_list=list()
    id=0
    def __init__( self ,name=''):
        self.brand_name = name
        self.brand_id=Brand.id
        Brand.is_empty_brand(self)

    def check_if_brand_id_is_found(self,brand_id):
        for i in range(len(Brand.Brands_list)):
            if brand_id==Brand.Brands_list[i]['brand_id']:
                # print(i)
                return True
        return False
    
    def is_empty_brand(self):
        if(self.brand_name==''):
            print('Your Brand Name is required !')
            return True
        Brand.Brands_list.append(
            {
                'brand_id':Brand.id,
                'brand_name':self.brand_name,
            }
        )
        Brand.id+=1
        return False

    def show_all_brands(self):
        for i in range(len(Brand.Brands_list)):
            print(f"Brand id : {Brand.Brands_list[i]['brand_id']}")
            print(f"Brand Name : {Brand.Brands_list[i]['brand_name']}")
            print('*'*20)
   

brand1=Brand('Brand1')
brand2=Brand('Brnad2')
brand3=Brand('Brand3')
# brand1.show_all_brands()