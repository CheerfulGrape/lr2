from dataclasses import dataclass

from data_types.host import Host
from data_types.vulnerability import Vulnerability


@dataclass
class Report:
    hosts: list[Host]
    vulnerabilities: list[Vulnerability]
