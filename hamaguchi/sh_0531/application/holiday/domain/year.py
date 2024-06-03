class Year:
    year:int
    validate:bool = False
    def __init__(self,year) -> None:
        self.year = int(year)
        
        self._validate()
        pass
    
    def validation(self):
        return self.validate
    
    
    def _validate(self):
        if self.year >= 2000 or self.year < 3001:
            self.validate = True
        