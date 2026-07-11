from models import PriceChange, PriceStatus

class PriceDetector:
    def compare(self,previous,current):
        changes=[]

        previous_map={p.product.title:p.product for p in previous}

        for snapshot in current:
            product=snapshot.product
            if product.title not in previous_map:
                continue

            old=previous_map[product.title]
            difference=product.price - old.price
            
            percentage=(difference/old.price)*100

            if difference>0:
                status=PriceStatus.INCRESED
            elif difference<0:
                status=PriceStatus.DECRESED
            else:
                status=PriceStatus.UNCHANGED

                
            changes.append(
                PriceChange(
                    title=product.title,
                    previoud=old.price,
                    current=product.price,
                    difference=round(difference,2),
                    percentage=round(percentage,2),
                    status=status
                )
            )
        
        return changes