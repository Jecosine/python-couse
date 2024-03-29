import os, json 
_products = {} 
_locations = {}
_items = [] 
 
def init(): 
    # read from json 
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
    # save products in json
    global _products 
    f = open("products.json", "w", encoding='utf-8') 
    f.write(json.dumps(_products, ensure_ascii=False)) 
    f.close() 
 
def _save_locations(): 
    # save location in json
    global _locations 
    f = open("locations.json", "w", encoding='utf-8') 
    f.write(json.dumps(_locations)) 
    f.close() 
 
def _save_items(): 
    # save item in json
    global _items 
    f = open("items.json", "w", encoding='utf-8') 
    f.write(json.dumps(_items)) 
    f.close() 
     
def get_products():  
    global _products 
    return _products 
 
def get_locations(): 
    global _locations 
    return _locations 
 
def get_items(): 
    global _items 
    return _items 
 
def add_product(sku_id, sku_name): 
    # add procuct
    global _products 
    _products[sku_id] = sku_name 
    _save_products() 
 
def add_location(loc_id, loc_name): 
    # add location
    global _locations 
    _locations[loc_id] = loc_name 
    _save_locations() 
 
def add_item(sku_id, loc_id): 
    # add an item
    global _items 
    _items.append((sku_id, loc_id)) 
    _save_items() 
 
def remove_item(sku_id, loc_id): 
    # pop an item
    global _items 
    for i in range(len(_items)): 
        if sku_id == _items[i][0] and loc_id == _items[i][1]: 
            del _items[i] 
            _save_items() 
            return True 
    return False 