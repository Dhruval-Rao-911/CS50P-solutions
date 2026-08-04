from project import get_total, view_by_category, add_expense
import os


def test_get_total_no_file():
    if os.path.exists("expenses.csv"):
        os.remove("expenses.csv")
    assert get_total() == 0


def test_get_total_with_data():
    with open("expenses.csv", "w") as f:
        f.write("2025-01-01,Food,100\n")
        f.write("2025-01-02,Travel,50\n")
    assert get_total() == 150


def test_functions_exist():
    assert callable(add_expense)
    assert callable(get_total)
    assert callable(view_by_category)
