"""Dictionary related utility functions."""

__author__ = "730245028"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Read that file
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close that file after you're done using it
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def head(rand_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Create a table with heading and first few rows."""
    result: dict[str, list[str]] = {}
    for key in rand_table:
        row_values: list[str] = []
        i: int = 0
        while i <= N:
            row_values.append(rand_table[key][i])
            i += 1
        result[key] = row_values
    return result


def select(rand_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Proudce a column based table with only specific columns."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = rand_table[name]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Cobine 2 tables."""
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            result[key] += table_2[key]
        else:
            result[key] = table_2[key]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Counts the frequencies of items."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in result:
            result[x[i]] += 1
        else:
            result[x[i]] = 1
        i += 1
    return result


def str_to_int(str_list: list[str]) -> list[int]:
    """Converts a list of str to list of int."""
    result: list[int] = []
    i: int = 0
    while i < len(str_list):
        result.append(int(str_list[i]))
        i += 1
    return result


def mean(x: list[int]) -> float:
    """Finds the average of a list of int."""
    result = sum(x) / len(x)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result