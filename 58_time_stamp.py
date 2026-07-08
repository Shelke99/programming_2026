# import time 
# while True:
#     # name = input("enter your name: ")
#     # print(".....Running....")
#     # if name == 'Priya':
#     #     continue
#     # break
#     # time.sleep(5)
#     passw = input("enter passward: ")
#     if passw == "priya123":
#         print("passward accepted...")
#         break 
#     else:
#         print("Enter the correct pass key, try again")
# Implement a command processor loop that exits on "quit"/"exit".
# def cmd_proc():
#     while True:
#         cmd = input("enter the num: ").strip().lower()

#         if cmd in ('quit', 'exit'):
#             print("exiting cmd processor")
#             break 
# print(cmd_proc())
import matplotlib.pyplot as plt

def get_user_data():
    """
    Collects category names and corresponding values from the user.
    Returns:
        categories (list): List of category labels.
        values (list): List of numeric values.
    """
    try:
        n = int(input("Enter number of categories: "))
        if n <= 0:
            raise ValueError("Number of categories must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None

    categories = []
    values = []

    for i in range(n):
        category = input(f"Enter name for category {i+1}: ").strip()
        try:
            value = float(input(f"Enter value for '{category}': "))
        except ValueError:
            print("Invalid value. Please enter a number.")
            return None, None
        categories.append(category)
        values.append(value)

    return categories, values

def draw_bar_chart(categories, values, orientation="vertical"):
    """
    Draws a bar chart based on user input.
    Args:
        categories (list): Category labels.
        values (list): Numeric values.
        orientation (str): 'vertical' or 'horizontal'.
    """
    plt.figure(figsize=(8, 5))
    if orientation.lower() == "horizontal":
        plt.barh(categories, values, color='skyblue', edgecolor='black')
        plt.xlabel("Values")
        plt.ylabel("Categories")
        plt.title("Horizontal Bar Chart")
    else:
        plt.bar(categories, values, color='lightgreen', edgecolor='black')
        plt.ylabel("Values")
        plt.xlabel("Categories")
        plt.title("Vertical Bar Chart")

    plt.grid(axis='x' if orientation.lower() == "horizontal" else 'y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    categories, values = get_user_data()
    if categories and values:
        chart_type = input("Enter chart type (vertical/horizontal): ").strip().lower()
        if chart_type not in ["vertical", "horizontal"]:
            print("Invalid chart type. Defaulting to vertical.")
            chart_type = "vertical"
        draw_bar_chart(categories, values, chart_type)
