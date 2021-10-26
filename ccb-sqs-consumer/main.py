import lambda_function


# Se debe cambiar el Trace ID en el campo "Body" (linea 10), de lo contrario fallará la prueba.
event = {
  "Records": [
    {
      "messageId": "dd7872f4-8f24-4472-9a72-3a1e56bd31fa",
      "receiptHandle": "AQEB3qHJdPWA80opCgIx5iTuQvtkFpXC4sGe0E3nvkjtDNmNx3uXQBi/+7caVHXV8nECJ8HF/xqEoM2DZ2X9mEHzXL62lShR6LY5rjgDpMK64aui/sP3V8fUjR3SB0zfrC33o2R5QS28cG27+rWdwg7alhFWz75fZG9DkobQQl/i9fThlmH/Si4cp+DR+XfpfWgQnxMFl8V+QXK2AUPcfTNEnvcMdpOprHme7Hm9N++AV773rpmWnFeqog5TUav6q+g4onik9p9wrYHYHNLAgIA+gNq1uOEqEZet6KYrVaDPU1/li8HaouTtP9GrX6gcQKu8WZrS6OHk6o7Ol0Q2+eDGCbEmmsiKH29k/5q0AowMFCsx6dscXGJnDFLbXsJyHuyz6Y22PFF2bP3bDiz2p/RDsw==",
      "body": "{\"data\": {\"resultset0\": [{\"balanceactual\": \"6492.20\", \"crlim\": \"5500\", \"descr\": \"CREDICORP VISA PLATINUM\", \"disponible_compras\": \"0.00\", \"disponible_retiro_efectivo\": \"0.00\", \"fecpagodue\": \"2020-01-15T00:00:00\", \"fecultecta\": \"2019-12-20T00:00:00\", \"fecultpago\": \"2019-12-12T00:00:00\", \"numcuenta\": \"0000004765340020328\", \"numtarjeta\": \"4765340008416734\", \"pago_minimo\": \"878.00\", \"puntos_al_dia\": \"0\", \"puntos_ultimo_estado\": \"0\", \"query_date\": \"2021-10-17T22:26:47.633000\", \"ultpago\": \"3.38\"}]}, \"date\": \"2021-10-18T03:26:47.766063\", \"duration\": \"164636\", \"input\": {\"accountId\": \"0000004765340020328\", \"company\": 1, \"country\": 1, \"creditCard\": \"4765340008416734\", \"format\": \"JSON\", \"queryDate\": \"2021-05-24\", \"source\": \"CCB\", \"sourceIP\": \"192.168.2.201\", \"trace_id\": \"aws-9c691b82-9359-4a9c-84ce-d9c9bed229ce\", \"yearMonth\": \"2021-05\"}, \"level\": \"TRACE\", \"name\": \"CCB_MSSQL_Python_Test\", \"success\": true}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1634527607908",
        "SenderId": "AROA25UCUNTOLD2N4AFVZ:CCB_MSSQL_Python_Test",
        "ApproximateFirstReceiveTimestamp": "1634527607918"
      },
      "messageAttributes": {},
      "md5OfBody": "65ec9caae83630a92c81417c7da58877",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:750819503324:ccb_services_logs",
      "awsRegion": "us-east-1"
    }
  ]
}


lambda_function.lambda_handler(event, None)


