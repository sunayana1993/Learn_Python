class chaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw="water, milk, ginger, honey"

cleaned=chaiUtils.clean_ingredients(raw)
print(cleaned)

