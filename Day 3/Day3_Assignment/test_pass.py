my_dict = {}


def find_pass_result():
    num = int(input("Enter the persons"))
    for i in range(0, num):
        id = int(input("Enter the id"))
        result = str(input("Enter the result"))
        name = str(input("Enter the name"))
        print({"id: {} result: {} name: {}".format(id, result, name)})
        if result == "pass":
            print(name)


find_pass_result()
