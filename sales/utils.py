import uuid


def generate_id():
    code = str(uuid.uuid4()).upper()[:12]
    return code
