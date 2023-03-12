
# I get the string value from the list #
def replacing_the_list(context, input_list):
    list_of_variable = []
    file_list = input_list.split(",")
    for variable in file_list:
        data = variable.replace("[", "").replace("'", "").replace("]", "")
        variable = data.split(",")
        if "((" in data:
            variable = variable[0]
            data = variable.replace("((", "")
        variable = data.split(",")
        variable = variable[0]
        list_of_variable.append(variable)
    return list_of_variable
