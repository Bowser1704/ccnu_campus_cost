from models import model
from utils.wc import generate
import json

if __name__ == "__main__":
    stu_num = "2018212576"
<<<<<<< HEAD
    cost = model.get_first_data(stu_num)
    print(json.dumps(cost))
    print(json.dumps(model.get_last_data(stu_num)))
    print(json.dumps(model.get_cost_sum(stu_num)))
    print(json.dumps(model.get_most_restaurant(stu_num)))
=======
    # cost = model.get_first_data(stu_num)
    # print(json.dumps(cost))
    # print(json.dumps(model.get_last_data(stu_num)))
    # print(json.dumps(model.get_cost_sum(stu_num)))
    # print(json.dumps(model.get_most_restaurant(stu_num)))
    print(json.dumps(model.get_cost_rank()))
    print(json.dumps(model.get_restaurant_place_rank()))
>>>>>>> cda0e9c65e6e7bfcc079e49e66e5575e575497f5
    # print(model.get_most_restaurant(stu_num))
    # generate.generate_place(stu_num)
