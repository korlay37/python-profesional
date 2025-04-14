
from datetime import datetime

# class LoggingMixin:
#     def log(self, message: str) -> None:
#         print(f"[{datetime.now().isoformat()}] {message}")

# class User(LoggingMixin):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def greet(self) -> None:
#         self.log(f"User {self.name} says hello")

# user = User("Eduardo")
# user.greet()

# class ValidationMixin:
#     def validate_name(self, name: str) -> bool:
#         return name.isalpha() and len(name) >= 3
    
# class Product(ValidationMixin):
#     def __init__(self, name: str) -> None:
#         if not self.validate_name(name):
#             raise ValueError("Nombre invalido")
#         self.name = name

# p = Product("1234")

class TimestampMixin:
    created_at: datetime

    def set_timestamp(self) -> None:
        self.created_at = datetime.now()

class File(TimestampMixin):
    def __init__(self, filename: str)-> None:
        self.filename = filename
        self.set_timestamp()

f = File("archivo.txt")
print(f.created_at)