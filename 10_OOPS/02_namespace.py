class chai:
    origin="India"

print(chai.origin)
chai.is_hot=True

masala=chai()
print(f"{masala.origin}")

masala.is_hot=False
print(f"object :{masala.is_hot}")
print(f"class is:{chai.is_hot}")