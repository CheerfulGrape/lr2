from dataclasses import dataclass
from datetime import datetime

from data_types.vulnerability import Vulnerability
from data_types.host import Host


@dataclass
class IncidentCard:
    """
    IncidentCard is a class containing all the information about the incident
    :ivar name incident name
    :ivar type_name type of incident
    :ivar event_count number of events, related to incident
    :ivar critical_rating critical rating
    :ivar vulnerabilities list of vulnerabilities
    :ivar hosts list of hosts
    :ivar start_date start date
    :ivar end_date end date
    """
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
