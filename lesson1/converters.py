class FourDigitYearConverter:
    regex = r"[0-9]{4}"

    def to_python(self,value):
        return int(value)
    
    def to_url(self,value):
        return "%04d" % value
    

class PhoneExtractConverter:
    regex = r"\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}"  # пример: +7(499)-777-77-77

    def to_python(self, value):
        digits = ''.join(filter(str.isdigit, value))
        return (int(digits[1:4]), int(digits[4:7]), int(digits[7:9]), int(digits[9:11]))  # Возвращаем кортеж из частей номера
    
    def to_url(self, value):
        return "+7(%03d)-%03d-%02d-%02d" % value  # Форматируем номер 