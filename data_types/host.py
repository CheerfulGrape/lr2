from dataclasses import dataclass


@dataclass
class Host:
    """
    Host class contains information about a particular host
    :ivar asset_id asset id
    :ivar type_name type of host
    :ivar host_name name of host
    :ivar user_account user account name
    """
    asset_id: int
    type_name: str
    host_name: str
    user_account: str

    def __str__(self):
        return f'({self.user_account}, {self.host_name}, {self.type_name})'
