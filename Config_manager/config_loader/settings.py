
# Internal file - Users should NOT import this directly!

_database_url = "postgres://user:pass@localhost:5432/mydb"
_api_key = "sk_live_123456789"
_debug_mode = True

def get_db():
    return _database_url

def get_key():
    return _api_key

def is_debug():
    return _debug_mode
