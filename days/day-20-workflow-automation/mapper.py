class FieldMapper:
    def __init__(self):
        self.mapping={
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email Address",
            "phone":"Phone Number",
        }

    def map(self,row):
        mapped={}
        for key, value in row.items():
            mapped[self.mapping.get(key, key)]=value 

        return mapped 
        