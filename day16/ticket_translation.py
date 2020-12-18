#!/usr/bin/env python3

import logging
import sys
from collections import defaultdict

# logging.basicConfig(format='  %(message)s  ', stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(format="  %(message)s  ", stream=sys.stderr, level=logging.INFO)


def clean_input(file) -> list:
    with open(file, "r") as f:
        input = f.read()
        input = input.replace(":\n", ":")
        logging.debug(input)
        rows = input.split("\n")
        return rows


def create_categories(lst: list):
    """
    split every thing into the 3 categories:
        my ticket
        tickets
        fields with values
    :param lst:
    :return my_ticket, valid_values, tickets:
    """
    values = {}
    ticket_lst = []
    my_ticket = []

    for row in lst:
        if ":" in row:
            if "your ticket" in row:
                my_ticket = row.split(":")[1]
            elif "nearby tickets" in row:
                ticket_lst.append(row.split(":")[1])
            else:
                field, value = row.split(":")
                values[field] = value
            logging.debug(row)
        else:
            if row != "":
                ticket_lst.append(row)
    ticket_lst = [[int(value) for value in ticket.split(",")] for ticket in ticket_lst]
    logging.debug(f"here are my {ticket_lst}")
    return my_ticket, values, ticket_lst


def organize_values(valid_values: dict):
    """
    clean up the values in valid_values and
    create a master comparison list for valid values
    :param valid_values:
    :return valid_values, tickets:
    """
    comparison_lst = []
    for field, value in valid_values.items():
        temp_lst = []
        values = value.replace(" ", "").split("or")
        logging.debug(values)
        for item in values:
            start, stop = item.split("-")
            temp_lst += [x for x in range(int(start), int(stop) + 1)]
        logging.debug(f"{temp_lst}")
        comparison_lst += temp_lst
        valid_values[field] = temp_lst
    return valid_values, comparison_lst


def answer_pt1(tickets: list, comparison_lst: list) -> int:
    """
    compares the tickets list to a master list of valid values and
    returns the total of all invalid values

    :param tickets:
    :param comparison_lst:
    :return total of all invalid values:
    """

    invalid_parameters = []
    logging.debug(f"tickets are {tickets}")
    logging.debug(f"master comparison list {comparison_lst}")
    for ticket in tickets:
        for parameter in ticket:
            if parameter not in comparison_lst:
                invalid_parameters.append(parameter)
    logging.debug(invalid_parameters)
    total = 0
    for parameter in invalid_parameters:
        total += parameter
    logging.debug(f"answer to pt1 is {total}")
    return total


def dump_invalid_tickets(tickets: list) -> list:
    valid_ticket_lst = []
    for ticket in tickets:
        if set(ticket).issubset(set(master_comparison_lst)):
            valid_ticket_lst.append(ticket)
    return valid_ticket_lst


def define_field_column(tickets: list, values: dict) -> dict:

    # Make the column values of the tickets accessible.
    columns = defaultdict(list)
    for ticket in tickets:
        logging.debug(f"valid ticket: {len(ticket)}")
        for column, number in enumerate(ticket):
            logging.debug(f"{column} - {number}")
            columns[column].append(number)

    # Map columns to the possible fields from the valid values.
    suggestions = defaultdict(list)
    for column, numbers in columns.items():
        for field, valid in values.items():
            if set(numbers).issubset(set(valid)):
                suggestions[field].append(column)
    return suggestions


def simplify_field_column(suggestions: dict) -> dict:

    # Whittle down suggestion to one column per field.
    final_fields = {}
    while len(final_fields) < len(suggestions):
        for field, columns in suggestions.items():
            if len(columns) == 1 and field not in final_fields.keys():
                final_fields[field] = columns[0]
                for k, v in suggestions.items():
                    while final_fields[field] in v:
                        suggestions[k].remove(final_fields[field])

    return final_fields


def answer_pt2(fields: dict, ticket: str):
    total = 1
    ticket = [int(x) for x in ticket.split(",")]
    for field, column in fields.items():
        if "departure" in field:
            total *= ticket[column]
    return total


if __name__ == "__main__":

    # start cleaning our input data
    # cleaned_input = clean_input("puzzle_input_test")
    cleaned_input = clean_input("puzzle_input")
    # cleaned_input = clean_input("puzzle_input_test_pt2")
    logging.info(cleaned_input)

    # split up the input into categories
    my_ticket, valid_values, ticket_list = create_categories(cleaned_input)
    logging.info(f"{my_ticket}, {valid_values}, {ticket_list}")

    # expand value ranges and create master_comparison_list
    valid_values, master_comparison_lst = organize_values(valid_values)
    logging.info(f"{valid_values} \n {set(master_comparison_lst)}")

    # get the answer to pt1
    logging.info(f"{answer_pt1(ticket_list, master_comparison_lst)}")

    # dump the invalid tickets
    valid_tickets = dump_invalid_tickets(ticket_list)
    logging.info(valid_tickets)

    # determine order the fields appear on ticket
    field_column = define_field_column(valid_tickets, valid_values)
    logging.info(f"{field_column}")

    field_column = simplify_field_column(field_column)
    logging.info(f"{field_column}")

    logging.info(f"{answer_pt2(field_column, my_ticket)}")
