sign_schema = {
    'type': 'object',
    'properties': {
        'path': {
            'type': 'string',
            'format': 'uri-reference'
        },
        'method': {
            'type': 'string',
            'enum': ['GET', 'POST', 'POST', 'DELETE']
        }
    },
    'required': ['path', 'method'],
    'additionalProperties': False
}