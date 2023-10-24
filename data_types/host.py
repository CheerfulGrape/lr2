from dataclasses import dataclass


@dataclass
class Host:
    asset_id: int
    type_name: str
    host_name: str
    user_account: str

    def __str__(self):
        return f'({self.user_account}, {self.host_name}, {self.type_name})'
