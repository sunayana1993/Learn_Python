def chai_counter():
    chai_order="lemon"
    def print_order():
        chai_order="ginger"
        print(f"Inner loop: {chai_order}")
    print(f"Outer scope:{chai_order}")
    print_order()

chai_order="Tulsi"
print(f"Out of function : {chai_order}")
chai_counter()