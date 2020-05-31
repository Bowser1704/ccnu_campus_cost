import wordcloud
import os
from models import model


# 生成词云
def generate(word_list, stu_num):
    module_path = os.path.dirname(__file__)
    wc = wordcloud.WordCloud(
        collocations=False,
        background_color='white',
        font_path=module_path + "/msyh.ttf",
    )
    wc.generate(word_list)
    wc.to_file(module_path + "/tmp/{}.png".format(stu_num))


def generate_restaurant(stu_num):
    return generate(' '.join(model.get_restaurant_list(stu_num)), stu_num)


def generate_place(stu_num):
    return generate(' '.join(model.get_place_list(stu_num)), stu_num)
