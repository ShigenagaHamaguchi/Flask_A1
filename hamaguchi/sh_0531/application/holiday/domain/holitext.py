import re

class HoliText:
    text:str
    validate: bool = False
    pattern = re.compile("^[ぁ-んァ-ン一-龠]+$")

    def __init__(self,text) -> None:
        self.text = text
        self._validation()

        pass
    def validation(self):
        return self.validate
    def _validation(self):
        if self.pattern.search(self.text):
            self.validate = True
    
class HoliTextVaildation(Exception):
    def __init__(self, message="holitextのバリデーション違反"):
        super().__init__(message)