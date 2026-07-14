from playwright.sync_api import Page 
from .models import MousePoint 

class MouseController:
    def click(self,page:Page,point:MousePoint):
        page.mouse.click(point.x,point.y)

    
    def hover(self,page:Page,point:MousePoint):
        page.mouse.move(point.x,point.y)

        