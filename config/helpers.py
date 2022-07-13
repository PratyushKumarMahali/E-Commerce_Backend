# find and call data in db
def serializeDict(arg) -> dict:
    return {**{item:str(arg[item]) for item in arg if item=='_id'},**{item:arg[item] for item in arg if item!='_id'}}
def serializeList(entity) -> list:
    return [serializeDict(arg) for arg in entity]