import hashlib

MAX_SUBMISSIONS = 4
MAX_CLOTH_COUNT = 25
def _md5(number):
    number_str = str(number).encode()
    md5_hash = hashlib.md5()
    md5_hash.update(number_str)
    return md5_hash.hexdigest()