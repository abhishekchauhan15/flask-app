from datetime import datetime
from bson.objectid import ObjectId

def todo_schema(data):
    return {
        'id': str(data.get('_id')),
        'name': data.get('name'),
        'description': data.get('description'),
        'created_at': data.get('created_at', datetime.utcnow())
    }
