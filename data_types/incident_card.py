from dataclasses import dataclass
from datetime import datetime

from data_types.vulnerability import Vulnerability
from data_types.host import Host


@dataclass
class IncidentCard:
    name: str
    type_name: str
    event_count: int
    critical_rating: float
    vulnerabilities: list[Vulnerability]
    hosts: list[Host]
    start_date: datetime
    end_date: datetime

    def __str__(self):
        return \
f'''Название: {self.name}
Тип: {self.type_name}
Количество событий, составляющих инцидент: {self.event_count}
Критичность: {self.critical_rating}
Название учётных записей и хостов и типы связанных активов: {', '.join([str(host) for host in self.hosts])}
Предполагаемые проэксплуатируемые уязвимости: {', '.join([vuln.title for vuln in self.vulnerabilities])}'''
