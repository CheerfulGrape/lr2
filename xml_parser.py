import os
from datetime import datetime, date
import xml.etree.ElementTree as ET

from data_types.report import Report, Host, Vulnerability


def parse_xml_report_file(path: str) -> Report:
    """
    Parse XML report file and produces a Report object
    :param path: path to xml file
    :raises RuntimeError on invalid xml format
    :return: report object of type Report
    """
    if not os.path.exists(path) or os.path.splitext(path)[1] != '.xml':
        raise RuntimeError(f'Invalid Input: File {path} does not exist or has wrong extension!')

    hosts = list[Host]()
    vulns = list[Vulnerability]()

    tree = ET.parse(path)
    root = tree.getroot()
    for group in root:
        if group.tag == 'server':
            continue # empty
        elif group.tag == 'tasks':
            continue # empty
        elif group.tag == 'hosts':
            for host in group:
                new_host = Host(0, '', '', '')
                for item in host:
                    if item.tag == 'asset_id':
                        new_host.asset_id = int(item.text)
                    else:
                        raise RuntimeError(f'Invalid Input: Unexpected host field "{item.tag}"!')
                hosts.append(new_host)
        elif group.tag == 'vulnerabilities':
            for vuln in group:
                new_vuln = Vulnerability('', '', '', '', '', date.today(), 0, 0, '')
                for item in vuln:
                    if item.tag == 'title':
                        new_vuln.title = item.text
                    elif item.tag == 'short_description':
                        new_vuln.short_desc = item.text
                    elif item.tag == 'description':
                        new_vuln.desc = item.text
                    elif item.tag == 'how_to_fix':
                        new_vuln.how_to_fix = item.text
                    elif item.tag == 'links':
                        new_vuln.links = item.text
                    elif item.tag == 'publication_date':
                        new_vuln.publication_date = datetime.strptime(item.text, '%Y-%m-%d').date()
                    elif item.tag == 'cvss':
                        new_vuln.cvss = float(item.text)
                    elif item.tag == 'cvss3':
                        new_vuln.cvss3 = float(item.text)
                    elif item.tag == 'global_id':
                        new_vuln.global_id = item.text
                    else:
                        raise RuntimeError(f'Invalid Input: Unexpected vulnerability field "{item.tag}"!')
                vulns.append(new_vuln)
        else:
            raise RuntimeError(f'Invalid Input: Unexpected report field "{group.tag}"!')

    return Report(hosts=hosts, vulnerabilities=vulns)
