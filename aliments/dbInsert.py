from aliments import dbRequests
from aliments.models import Category
from aliments.models import Store
from aliments.models import Products
from aliments.models import Foodsave
# from aliments.models import User


def insertCategory():
    category_list = {}
    cat_list = []
    request = dbRequests.DbRequests()

    category_list = request.Request_categories()

    for i in category_list:
        idcat = i['id']
        name = i['nameCategory']
        cat = Category(nameCategory=name, idCategory=idcat)

        cat_list.append(cat)

    # Call bulk_create to create records in a single call
    Category.objects.bulk_create(cat_list)


def insertStore():
    store_list = {}
    sto_list = []

    request = dbRequests.DbRequests()

    store_list = request.Request_stores()

    for i in store_list:
        idSto = i['id']
        name = i['nameStore']
        store = Store(nameStore=name, idStore=idSto)

        sto_list.append(store)

    # Call bulk_create to create records in a single call
    Store.objects.bulk_create(sto_list)


def insertProducts():
    list_prod_obj = []

    request = dbRequests.DbRequests()

    product_list = request.Request_products()
    #print(product_list)
    for i in product_list:
        nameAlim = i["nameAlim"]
        image = i["image"]
        url = i["url"]
        descriptionAlim = i["descriptionAlim"]
        nutritionGrade = i["nutritionGrade"]
        idCategory = i["idCategory"]
        idStore = i["idStore"]

        # get id category for this product
        idCat = getidCategory(idCategory)
        # get id store for this product
        idSto = getidStore(idStore)
        print(idCat.idCategory)
        print(idSto.idStore)
        
        if (idCat is not None) and (idSto is not None):
            product = Products(nameAlim=nameAlim, image=image, url=url, 
                               descriptionAlim=descriptionAlim, 
                               nutritionGrade=nutritionGrade, idCategory=idCat, 
                               idStore=idSto)
        
            list_prod_obj.append(product)
    
            # Call bulk_create to create records in a single call
            Products.objects.bulk_create(list_prod_obj)
        else:
            continue


def getidCategory(category):
    print(category)
    id_Category = Category.objects.filter(nameCategory=category)
    print(id_Category.values)
    if id_Category.first():
        obj_cat_id = id_Category
        obj_cat = Category(idCategory=obj_cat_id, nameCategory=category)
    else:
        obj_cat = None
    print(obj_cat.idStore)
    return(obj_cat)


def getidStore(store):
    print(store)
    id_Store = Store.objects.filter(idStore=store)
    print(id_Store.values)
    if id_Store.first():
        obj_Sto_id = id_Store
        obj_store = Store(idStore=obj_Sto_id,nameStore=store)
    else:
        obj_store = None
    print(obj_store.idStore)
    return(obj_store)


def insertUser():
    pass