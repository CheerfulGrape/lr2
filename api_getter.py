import requests

from data_types.host import Host


def get_asset_info(asset_id: int) -> Host:
    obj = Host(0, '', '', '')
    API_str = "https://d5d9e0b83lurt901t9ue.apigw.yandexcloud.net"
    r = requests.get(
        f'{API_str}/get-asset-by-id',
        {'asset-id': asset_id}
    )
    row = r.json()['result']
    obj.asset_id = asset_id
    obj.user_account = row["account_name"]
    obj.type_name = row["equipment_type"]
    obj.host_name = row['hostname']
    return obj
