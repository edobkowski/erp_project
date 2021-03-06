def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    number_of_columns = len(title_list)
    cell_widths = calculate_width(table, number_of_columns)
    cell_content = "{:^" + str(cell_widths[0]) + "}"
    break_line = "-" * 4 + "-" * sum(cell_widths)

    print (break_line)
    for i in range(number_of_columns):
        cell_content = "{:^" + str(cell_widths[i]) + "}"
        print ("|" + cell_content.format(title_list[i]), end = "")
    print("|")
    print (break_line)

    for i in table:
        print (break_line)
        for j in range(number_of_columns):
            cell_content = "{:^" + str(cell_widths[j]) + "}"
            print ("|" + cell_content.format(i[j]), end = "")
        print("|")
    print (break_line)


def calculate_width(table, n):
    arr = []
    for i in range(n):
        max_string_len = max(table,key = lambda x: len(str(x[i])))
        arr.append(len(max_string_len[i]) + 4)
    return arr


def print_result(result):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """


    print(title,":")
    i = 0
    x = 1
    while i != len(list_options):
        print("(",str(x),")", list_options[i])
        i += 1
        x += 1
    print("( 0 )",exit_message)

    pass


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for i in list_labels:
        inputs.append(input(i))
    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(message)

    pass
