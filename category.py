class Category:
    categorys_list=list()
    id=0
    def __init__( self ,name):
        self.category_name = name
        self.category_id=Category.id
        Category.is_empty_category(self)
    def is_empty_category(self):
        if(self.category_name==''):
            print('Your category Name is required !')
            return True
        Category.categorys_list.append(
            {
                'category_id':Category.id,
                'category_name':self.category_name,
            }
        )
        Category.id+=1
        return False
    
    def check_if_category_id_is_found(self,category_id):
        for i in range(len(Category.categorys_list)):
            # print(i)
            if category_id==Category.categorys_list[i]['category_id']:
                # print('True')
                return True
        return False
    
    def show_all_categorys(self):
        for i in range(len(Category.categorys_list)):
            print(f"category Name : {Category.categorys_list[i]['category_name']}")
   

category1=Category('category1')
category2=Category('cateory2')
category3=Category('category3')
# category3.show_all_categorys()
# print(category3.show_all_categorys())