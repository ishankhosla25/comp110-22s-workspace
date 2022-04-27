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


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
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