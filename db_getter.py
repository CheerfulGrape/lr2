import os
import pandas as pd
from sqlalchemy import create_engine, text

from data_types.incident_card import IncidentCard


def get_incident_from_db(incident_id: str = '231830') -> (IncidentCard, list[int], list[int]):
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_URL')
    port = os.getenv('DB_PORT')
    db_name = 'db1'
    DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(DATABASE_URL, connect_args={'sslmode': 'require'})

    query = text(f"SELECT * FROM sitii_lr2_incidents WHERE id = '{incident_id}'")

    with engine.begin() as conn:
        res = pd.read_sql_query(query, conn)
    res_dict = res.to_dict()

    pd.set_option("display.expand_frame_repr", False)

    return IncidentCard(name=res_dict['name'][0],
                        type_name=res_dict['type'][0],
                        event_count=res_dict['events_count'][0],
                        critical_rating=res_dict['crit_rate'][0],
                        vulnerabilities=[],
                        hosts=[],
                        start_date=res_dict['start_time'][0],
                        end_date=res_dict['end_time'][0]), res_dict['assets_id'][0], res_dict['vulnerabilities_id'][0]
