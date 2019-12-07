import data 
 
def prompt_for_action(): 
    """ 提示功能菜单。返回用户输入选择 """ 
    while True: 
        print('---------------库存信息管理系统-------------') 
        print('| 1: 增加产品信息                          |') 
        print('| 2: 产品信息报表                          |') 
        print('| 3: 增加货架位置                          |') 
        print('| 4: 货架位置报表                          |') 
        print('| 5: 商品入库管理                          |') 
        print('| 6: 商品出库管理                          |') 
        print('| 7: 商品库存信息报表                      |') 
        print('| 0: 退出                                 |') 
        print('-------------------------------------------') 
         
        choice = input('请选择功能菜单(0-7):') 
        if choice == '0': return 'QUIT' 
        elif choice == '1': return 'ADD_PRODUCT' 
        elif choice == '2': return 'REPORT_PRODUCTS' 
        elif choice == '3': return 'ADD_LOCATION' 
        elif choice == '4': return 'REPORT_LOCATIONS' 
        elif choice == '5': return 'ADD_ITEM' 
        elif choice == '6': return 'REMOVE_ITEM' 
        elif choice == '7': return 'REPORT_ITEMS' 
 
def prompt_for_old_sku_id(): 
    """ 提示用户输入有效的产品sku_id并返回有效产品ID，或者返回None """ 
    while True: 
        sku_id = input("请输入产品ID:") 
        if sku_id == "":  
            return None 
        elif sku_id not in data.get_products():  
            print("该产品不存在, 请重新输入") 
        else: 
            return sku_id 
 
def prompt_for_new_sku_id(): 
    """ 提示用户输入新的产品sku_id并返回新产品ID，或者返回None """ 
    while True: 
        sku_id = input("请输入新的产品ID:") 
        if sku_id == "": return None 
        elif sku_id in data.get_products():  
            print("该产品已经存在,请重新输入") 
        else: 
            return sku_id 
 
def prompt_for_old_loc_id(): 
    """ 提示用户输入有效的货架位置loc_id并返回有效货架位置ID，或者返回None """ 
    while True: 
        loc_id = input("请输入货架位置ID:") 
        if loc_id == "":  
            return None 
        elif loc_id not in data.get_locations():  
            print("该货架位置不存在,请重新输入") 
        else: 
            return loc_id 
 
def prompt_for_new_loc_id(): 
    """ 提示用户输入新的货架位置loc_id并返回，或者返回None """ 
    while True: 
        loc_id = input("请输新的货架位置ID:") 
        if loc_id == "": return None 
        elif loc_id in data.get_locations():  
            print('该货架位置已经存在,请重新输入') 
        else:  
            return loc_id 
 
def prompt_for_sku_name(): 
    """ 提示用户输入产品名称sku_name并返回产品名称，或者返回None """ 
    while True: 
        sku_name = input("请输入产品名称:") 
        if sku_name == "": return None 
        else: return sku_name 
 
def prompt_for_loc_name(): 
    """ 提示用户输入货架位置名称loc_name并返回货架位置名称，或者返回None """ 
    while True: 
        loc_name = input("请输入货架位置名称:") 
        if loc_name == "": return None 
        else: return loc_name 
 
def report_products(): 
    """ 产品信息报表 """ 
    for (k, v) in data.get_products().items(): 
        print('{0:8}  {1}'.format(k, v)) 
 
def report_locations(): 
    """ 货架位置报表 """ 
    for (k, v) in data.get_locations().items(): 
        print('{0:8}  {1}'.format(k, v)) 
 
def report_items(): 
    """ 库存信息报表 """ 
    for (k, v) in data.get_items(): 
        sku_name = data.get_products()[k] 
        loc_name = data.get_locations()[v] 
        print('{0:8} {1}： {2:8}{3}'.format(k,sku_name,v,loc_name)) 
CS10.5 数据处理模块data.py的实现 
数据处理模块实现表CS-1所示的API。通过Python标准库模块json中的
loads()函数和dumps()函数，可以实现从JSON文件读取数据和转储数据到JSON
文件的功能。 
【例CS.33】库存管理系统数据处理模块data.py。 
import os 
import json 
 
#全局变量 
_products = {} #保存产品信息的字典：sku_id:sku_name 
_locations = {} #保存货架位置的字典：loc_id:loc_name 
_items = [] #保存商品库存的列表，元素为元组(sku_id,loc_id) 
 
def init(): 
    """从磁盘JSON格式文件中读取数据""" 
    global _products, _locations, _items 
    if os.path.exists("products.json"): 
        f = open("products.json", "r", encoding='utf-8') 
        _products = json.loads(f.read()) 
        f.close() 
    if os.path.exists("locations.json"): 
        f = open("locations.json", "r", encoding='utf-8') 
        _locations = json.loads(f.read()) 
        f.close() 
    if os.path.exists("items.json"): 
        f = open("items.json", "r", encoding='utf-8') 
        _items = json.loads(f.read()) 
        f.close() 
         
def _save_products(): 
    """ 把产品信息数据_products以JSON格式保存到磁盘文件""" 
    global _products 
    f = open("products.json", "w", encoding='utf-8') 
    f.write(json.dumps(_products, ensure_ascii=False)) 
    f.close() 
 
def _save_locations(): 
    """ 把货架位置数据_locations以JSON格式保存到磁盘文件""" 
    global _locations 
    f = open("locations.json", "w", encoding='utf-8') 
    f.write(json.dumps(_locations)) 
    f.close() 
 
def _save_items(): 
    """ 把商品库存数据_items以JSON格式保存到磁盘文件""" 
    global _items 
    f = open("items.json", "w", encoding='utf-8') 
    f.write(json.dumps(_items)) 
    f.close() 
     
def get_products(): 
    """ 返回产品信息 """ 
    global _products 
    return _products 
 
def get_locations(): 
    """ 返回货架位置信息 """ 
    global _locations 
    return _locations 
 
def get_items(): 
    """ 返回商品库存信息 """ 
    global _items 
    return _items 
 
def add_product(sku_id, sku_name): 
    """ 增加一个产品sku_id、sku_name """ 
    global _products 
    _products[sku_id] = sku_name 
    _save_products() 
 
def add_location(loc_id, loc_name): 
    """ 增加一个货架位置loc_id、loc_name """ 
    global _locations 
    _locations[loc_id] = loc_name 
    _save_locations() 
 
def add_item(sku_id, loc_id): 
    """ 入库一件商品：商品sku_id、货架sku_id """ 
    global _items 
    _items.append((sku_id, loc_id)) 
    _save_items() 
 
def remove_item(sku_id, loc_id): 
    """出库一件商品：商品sku_id、货架sku_id，返回True；如果不存在，返回False""" 
    global _items 
    for i in range(len(_items)): 
        if sku_id == _items[i][0] and loc_id == _items[i][1]: 
            del _items[i] 
            _save_items() 
            return True 
    return False