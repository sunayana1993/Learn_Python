
def update_order():
    chai_type="Elaichi"
    def generate_order():
        nonlocal chai_type
        chai_type="ginger"
    generate_order()
    print(f"chai type is {chai_type}")

update_order()