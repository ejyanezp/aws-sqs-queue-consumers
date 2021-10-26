import json
from datetime import datetime
from ccb_toolbox import ccb_global, ccb_sql


connection_data = ccb_global.get_parameters(["/qa/sql/2016/globals", "/qa/sql/2016/apiservicelogs"])
conn = ccb_sql.connect(connection_data)


def lambda_handler(event, context):
    print(f"Event type: type(event)\nEvent: {event}")
    for record in event['Records']:
        body = json.loads(record['body'])
        print(body['date'])
        record_timestamp = datetime.fromisoformat(body['date'].replace('T', ' '))
        params = (body['input']['trace_id'], record_timestamp, body['duration'],
                  body['level'], body['name'], str(body['data']), body['input']['source'],
                  str(body['input']), body['input']['trace_id'])
        # print(f"Params: {params}")
        conn.cursor().execute("insert into [dbo].[service_usage] values (?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?)", params)
        conn.cursor().commit()
