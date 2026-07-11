from playwright.sync_api import Page
from .models import Product 

class ProductExtractor:
    def extract(self, page:Page, product_selector:str,title_selector:str, price_selector:str):
        products=[]
        cards=page.locator(product_selector).all()

        for card in cards:
            try:
                title=card.locator(title_selector).inner_text()

                price=card.locator(price_selector).inner_text()

                numeric=float("".join(c for c in price if c.isdigit() or c=="."))

                products.append(
                    Product(title=title,price=numeric,currency="USD",url=page.url)
                )
            except Exception as e:
                continue

        
        return products


                
