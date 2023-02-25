import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt', 'r') as file1:
        result = 'PASSWORD NOT IN DATABASE';
        datalist1 = file1.readlines()
        if (use_salts == False):
            for data1 in datalist1:
                tmp1 = data1.rstrip('\n').encode("utf-8")
                tmp2 = hashlib.sha1(tmp1).hexdigest()
                if (tmp2 == hash):
                    result = data1
                    break
            return result
        else:
            with open('known-salts.txt', 'r') as file2:
                datalist2 = file2.readlines()
                for data1 in datalist1:
                    for data2 in datalist2:
                        tmp1 = data2.rstrip('\n').encode("utf-8")
                        tmp2 = data1.rstrip('\n').encode("utf-8")
                        tmp3 = tmp1 + tmp2
                        tmp4 = hashlib.sha1(tmp3).hexdigest()
                        if (tmp4 == hash):
                            result = data1
                            break
                return result