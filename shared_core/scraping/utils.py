
def normalize_price(text:str):
    value="".join(c for c in text if c.isdigit() or c==".")

    return float(value)