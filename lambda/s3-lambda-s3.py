
event = {'Records': [
    {
        'eventVersion': '2.1',
        'eventSource': 'aws:s3',
        'awsRegion': 'ap-south-1',
        'eventTime': '2025-11-08T16:11:13.512Z',
        'eventName': 'ObjectCreated:Copy',
        'userIdentity': {'principalId': 'A33A27L3BCVCZL'},
        'requestParameters': {'sourceIPAddress': '49.207.227.203'},
        'responseElements': {'x-amz-request-id': '1K2BPBN85C70KG6D',
                             'x-amz-id-2': 'NHSEPGTBsyq8zah17Qgok0cPZXn0gXu3Ab9Jxy/mkCTyH8YQIlcCGC2GwvLJ4ftaMLd1ZEQ+DUAlRRpLUsXlAs7u/rq7DSPdtqVVFPgRoOE='},
        's3': {
            's3SchemaVersion': '1.0',
            'configurationId': '4c40dfc7-2797-4d01-beb4-b4105667af1a',
            'bucket': {'name': 's3-jyotsna', 'ownerIdentity': {'principalId': 'A33A27L3BCVCZL'},'arn': 'arn:aws:s3:::s3-jyotsna'},
            'object': {'key': 'bronze/employees.csv', 'size': 3778, 'eTag': '4f0d7e6a820dce97411d7020585cb675',
                          'sequencer': '00690F6BA17725F3E4'}
               }
    }
]
}

from lambda_function import lambda_handler
lambda_handler(event,None)
