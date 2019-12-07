import requests
from bs4 import BeautifulSoup as bs
import time, random
import os, re
url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={}&pn={}&gsm=&ct=&ic=0&lm=-1&width=0&height=0"
count = 0
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    #'Cookie': 'winWH=%5E6_1535x744; BDIMGISLOGIN=0; BAIDUID=26814D6AA96F8C498C9521D00C31619F:FG=1; BIDUPSID=26814D6AA96F8C498C9521D00C31619F; PSTM=1532750639; MCITY=-%3A; BDUSS=M4bURnMXcxa1BYeS1aNnZiQXZhanpxeFhNLVVhZXRvdzcydXI4aHZwcGpmLXBjRVFBQUFBJCQAAAAAAAAAAAEAAAAkLdgTenNtb2ppYW54aW5nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPywlxj8sJcMn; __cfduid=d6f922f49ef6763ae33cb99fa25eb2bdd1563979839; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; indexPageSugList=%5B%22%E5%BE%AE%E8%BD%AF%20logo%22%2C%22%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%20logo%22%2C%22%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%22%2C%22%E5%BE%AE%E8%BD%AF%22%2C%22Intel%22%2C%22Intel%20ncs%22%2C%22Intelncs%22%2C%22ncs%22%2C%22%E6%A0%91%E8%8E%93%E6%B4%BE%22%5D; delPer=0; PSINO=7; H_PS_PSSID=1437_21108_30211_20698; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm'
}
def get_links(img_count = 50, item = '%E7%8C%AB'):
    global url, count
    count = 0
    link_set = []
    
    for i in range(20):
        if count > img_count:
            break
        page = i * 20
        print "Start fetching page {}...".format(i)
        try:
            req = requests.get(url.format(item, page), headers = header, timeout=10)
            html = req.text
            
        except Exception as e:
            print "Error Occur: {}".format(e)
        else:
            # bsobj = bs(html, 'html.parser')
            # print bsobj
            # break
            links = re.findall('"objURL":"(.*?)",', html, re.S)
            if len(links) == 0:
                print "No Image link Found"
            else:
                
                count += len(links)
                #print links
        time.sleep(random.random()*2)
    c = ''
    for i in links[:img_count]:
        c += i + '\n'
    print c
    with open("links.txt", 'wb') as f:
        print os.listdir('.')
        
        print img_count
        
        f.write(c.encode('utf-8'))
    return links

def get_imgs(img_dir = 'Data'):
    with open("links.txt", 'rb') as f:
        content = f.read().decode('utf-8')
    link_set = [i for i in content.split('\n') if len(i) > 0]
    print "Getting images"
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    for i in range(len(link_set)):
        print "\tGetting {} th image".format(i)
        time.sleep(random.random() * 2)
        header['Referer'] = link_set[i]
        try:
            resp = requests.get(link_set[i], headers = header, timeout = 10)
            content = resp.content
            ext = resp.headers.get('Content-Type').split('/')[-1]
        except Exception as e:
            print "Error Occurred: {}".format(e)
        else:
            # format file ext name
            if not ext:
                ext = 'jpg'
            path = os.path.join(img_dir, "{}.{}".format(i, ext))
            with open(path, 'wb') as f:
                f.write(content)
            
#get_links()
get_imgs()
    
            
