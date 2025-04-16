# Instrucciones:
# Crea la clase AdminUser, que hereda de RegularUser.
# En el __init__, agrega permisos especiales como ["read", "write", "delete", "admin"].
# Redefine has_permission() para que siempre devuelva True.
# Escribe un pequeño bloque de código para:
# Crear un RegularUser y un AdminUser.
# Llamar a login() para ambos.
# Probar permisos con has_permission().

from abc import ABC, abstractmethod
from datetime import datetime

class UserBase(ABC):
    def __init__(self, email: str, password: str) -> None:
        super().__init__()
        self._email: str = email
        self._password: str = password
        self._permissions: list[str] = []

    @property
    def email(self) -> str:
        return self._email
    
    @abstractmethod
    def login(self) -> bool:
        pass

    @abstractmethod
    def has_permission(self, perm: str) -> bool:
        pass

class TimestampMixin:
    def __init__(self) -> None:
        super().__init__()
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
    
    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()

class LoggingMixin:
    def __init__(self) -> None:
        super().__init__()

    def log(self, msg: str) -> None:
        print(f"[LOG] {datetime.now().isoformat()} - {msg}")

class RegularUser(UserBase, TimestampMixin, LoggingMixin):
    def __init__(self, email: str, password: str) -> None:
        super().__init__(email, password)

    def login(self) -> bool:
        self.log(f"Usuario regular {self.email} inicio sesion")
        return True
    
    def has_permission(self, perm: str) -> bool:
        return perm in self._permissions
    
class AdminUser(RegularUser):
    def __init__(self, email: str, password: str) -> None:
        super().__init__(email, password)
        self._permissions = ["read", "write", "delete", "admin"]
    
    def login(self) -> bool:
        self.log(f"Usuario administrador {self.email} inicio sesion")
        return True
    
    def has_permission(self, perm: str) -> bool:
        return True
    
user1: RegularUser = RegularUser("email@gmail.com","pass123")
user2: AdminUser = AdminUser("admin@gmail.com","adminpass123")

user1.login()
user2.login()

print(user1.has_permission("delete"))
print(user2.has_permission("admin"))