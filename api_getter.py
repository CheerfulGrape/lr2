import os
import requests

from data_types.host import Host


def get_asset_info(asset_id: int) -> Host:
    """
    Get asset info from API (api URL should be in env variable 'API_URL')
    :param asset_id: id of an asset
    :return: Host object with asset information
    """
    host = Host(0, '', '', '')
    api_url = os.getenv('API_URL')
    r = requests.get(
        f'{api_url}/get-asset-by-id',
        {'asset-id': asset_id}
    )
    row = r.json()['result']
    host.asset_id = asset_id
    host.user_account = row["account_name"]
    host.type_name = row["equipment_type"]
    host.host_name = row['hostname']
    return host
