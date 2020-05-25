import wordcloud
import os
from models import model


def generate(word_list, stunum):
    module_path = os.path.dirname(__file__)
    wc = wordcloud.WordCloud(
        collocations=False,
        background_color='white',
        font_path=module_path + "/msyh.ttf",
    )
    wc.generate(word_list)
    wc.to_file(module_path + "/tmp/{}.png".format(stunum))


def generate_restaurant(stunum):
    return generate(' '.join(model.get_restaurant_list(stunum)), stunum)


def generate_place(stunum):
    return generate(' '.join(model.get_place_list(stunum)), stunum)
