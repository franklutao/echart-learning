from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

a = [list(z) for z in zip(Faker.guangdong_city, Faker.values())]
print(a)
c = (
    Map()
    .add("商家A", a, "广东")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guangdong.html")
)