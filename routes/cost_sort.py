
from pyecharts.charts import Bar

def get_html():

    def label_formatter(params):
        return params.data + '分'

    v1 = []   #学号
    attr = []   #总消费
    bar = Bar('testBar_color', 'Theme', page_title='人均消费排名')
    # 注意 label_color的属性值为 list(列表)
    bar.add("test_X", attr, v1, is_label_show=True, label_color=['#5AB5FF'], label_text_color='#3367FF',
            label_formatter=label_formatter)
    bar.render()



if __name__ == "__main__":
    get_html()

