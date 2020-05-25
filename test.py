from models import model
from utils.wc import generate

if __name__ =="__main__":
    stunum = "2018212576"
    # print(model.get_first_data(stunum))
    # print(model.get_most_restaurant(stunum))
    generate.generate_place(stunum)