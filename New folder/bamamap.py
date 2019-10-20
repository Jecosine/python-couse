from pyecharts import options as opts 
from pyecharts.charts import Map 
import random, csv
from pyecharts.charts import Geo
from pyecharts.globals import ChartType 



from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


class Data: 
    guangdong_city = ["佛山市","湛江市","潮州市","河源市","江门市", "中山市", "珠海市", "深圳市","东莞市","韶关市", "清远市", "云浮市", "茂名市","汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市","梅州市"]
    @staticmethod
    def values(start:int = 10, end:int = 40)->list:
        return [random.randint(start, end) for i in range(21)]
#class Data1:

# def loadcsv():
#     provinces = []
#     data = {2018: [], 2017: [], 2016: []}
#     with open("datata.csv",'r') as f:
#         content = csv.reader(f)    
#         for i in content:
#             provinces.append(i[0])
#             data[2018].append(float(i[1]))
#             data[2017].append(float(i[2]))
#             data[2016].append(float(i[3]))
#     return provinces, data
# p, d = loadcsv()
# class Data1:
#     global p
#     global d
#     provinces = p
#     @staticmethod
#     def get_values(y:int)->list:
#         return d[y]

def mp() -> Map:
    c = (
        Map()
        .add("2018", [list(i) for i in zip(Data1.provinces, Data1.get_values(2018))], "china")
        .add("2017", [list(i) for i in zip(Data1.provinces, Data1.get_values(2017))], "china")
        .add("2016", [list(i) for i in zip(Data1.provinces, Data1.get_values(2016))], "china")
        .set_global_opts(
            title_opts = opts.TitleOpts(title="Map"),
            visualmap_opts = opts.VisualMapOpts(min_=0, max_=100)
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return c
def heat(date)->Geo:
    return (
        Geo()
        .add_schema(maptype="广东")
        .add(
            "8月", [list(i) for i in zip(Data.guangdong_city, Data.values())], type_=ChartType.HEATMAP
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=42, is_piecewise=True),
            title_opts=opts.TitleOpts(title="广东"+date+"各地区温度变化情况")
        )
    )


path = "8月{0}日"
for i in range(5):
    #heat().render(path.format(i+1))+ ".html")
    make_snapshot(snapshot, heat(path.format(i+1)).render(), path.format(i+1)+".png", pixel_ratio=1)
