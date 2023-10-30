from dataclasses import dataclass

from data_types.host import Host
from data_types.vulnerability import Vulnerability


@dataclass
class Report:
    """
    Report is a class containing information about a certain security report related to the host(s) containing
    information from the report
    :ivar hosts relevant hosts
    :ivar vulnerabilities list of related vulnerabilities
    """
    hosts: list[Host]
    vulnerabilities: list[Vulnerability]
