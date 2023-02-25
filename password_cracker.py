import hashlib

def crack_sha1_hash(hash):
    with open('top-10000-passwords.txt', 'r') as file:
        datalist = file.readlines()
        result = 'PASSWORD NOT IN DATABASE';
        for data in datalist:
            if (hashlib.sha1(data.rstrip('\n').encode("utf-8")).hexdigest() == hash):
                result = data
                break
        return result