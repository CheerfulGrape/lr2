from db_getter import get_incident_from_db
from api_getter import get_asset_info
from xml_parser import parse_xml_report_file

from data_types.incident_card import IncidentCard


def get_incident_card(incident_id: str = '231830') -> IncidentCard:
    """
    Get incident card with aggregated info from a database, XML files and API
    :param incident_id: id of an incident (231830 is the default value)
    :return: IncidentCard object, containing information about the incident
    """
    card: IncidentCard
    card, asset_ids, vuln_ids = get_incident_from_db(incident_id)

    processed_vulns = []
    for asset_id in asset_ids:
        report = parse_xml_report_file(f'./lr2-xml/asset_{asset_id}_vuln_report.xml')
        for vuln in report.vulnerabilities:
            if vuln.global_id in vuln_ids and vuln.global_id not in processed_vulns:
                processed_vulns.append(vuln.global_id)
                card.vulnerabilities.append(vuln)
        card.hosts.append(get_asset_info(asset_id))
    return card
