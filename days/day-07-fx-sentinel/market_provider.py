import requests

class MarketProvider:
    BASE_URL="https://api.frankfurter.app/latest"

    def get_rate(self,base:str,target:str):
        response=requests.get(self,BASE_URL, params={"from":base,"to":target},timeout=10        )
        response.raise_for_status()
        data=response.json()
        
        return data["rates"][target]

        