from datetime import datetime
from .models import (ProductSnapshot)

class SnapshotManager:
    def create(self,product):
        return ProductSnapshot(
            product=product,
            timestamp=datetime.now()
        )