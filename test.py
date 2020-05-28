from models import model
from utils.wc import generate
import json

if __name__ == "__main__":
    stu_num = "2018212576"
    # cost = model.get_first_data(stu_num)
    # print(json.dumps(cost))
    # print(json.dumps(model.get_last_data(stu_num)))
    # print(json.dumps(model.get_cost_sum(stu_num)))
    # print(json.dumps(model.get_most_restaurant(stu_num)))
    # print(json.dumps(model.get_cost_rank()))
    # print(json.dumps(model.get_restaurant_place_rank()))
    # print(model.get_most_restaurant(stu_num))
    # generate.generate_place(stu_num)
    print(model.get_restaurant_rank(stu_num))
