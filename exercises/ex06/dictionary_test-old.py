# """Tests for Dictionary Functions!"""
# __author__ = '730245028'

# from dictionary import invert, favorite_color, count


# def test_invert_multiple_items() -> None:
#     """Tests if multiple items are inverted."""
#     random_dict: dict[str, str] = dict()
#     random_dict = {"A": "B", "C": "D", "E": "F"}
#     assert invert(random_dict) == {'B': 'A', 'D': 'C', 'F': 'E'}


# def test_invert_numeric_str() -> None:
#     """Tests if numeric strs are still inverted."""
#     random_dict: dict[str, str] = dict()
#     random_dict = {"1": "2", "3": "4"}
#     assert invert(random_dict) == {"2": "1", "4": "3"}

#     # def test_invert_duplicate_keys() -> None:
# #     """Tests whether duplicate keys returns an error!"""
# #     random_dict: dict[str, str] = dict()
# #     random_dict = {"A": "B", "C": "B", "E": "F"}
# #     assert invert(random_dict) == KeyError