str1="Sunayana"
str2="chai"
print(f"{str1} loves {str2}")

#we will also learn slicing of the string

#core,indexing,slicing
#strings are immutable
chai_description="Aromatic and Bold"
print(chai_description[0:7])
print(chai_description[0:7:2])
print(chai_description[:7])
print(f"Last word: {chai_description[12:]}")
print(f"reverse: {chai_description[::-1]}")

#using special character
lable_text="chai spécial"
encoded_label=lable_text.encode("utf-8")
print(f"encoded text {encoded_label}")
decoded_label=encoded_label.decode("utf-8")
print(f"decoded text {decoded_label}")