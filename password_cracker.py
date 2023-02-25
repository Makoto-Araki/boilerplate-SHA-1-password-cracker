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
                    result = data1.rstrip('\n')
                    break
            return result
        else:
            with open('known-salts.txt', 'r') as file2:
                datalist2 = file2.readlines()
                for data1 in datalist1:
                    for data2 in datalist2:
                        tmp1 = data1.rstrip('\n').encode("utf-8")
                        tmp2 = data2.rstrip('\n').encode("utf-8")
                        tmp3 = tmp2 + tmp1
                        tmp4 = tmp1 + tmp2
                        tmp5 = hashlib.sha1(tmp3).hexdigest()
                        tmp6 = hashlib.sha1(tmp4).hexdigest()
                        if (tmp5 == hash or tmp6 == hash):
                            result = data1.rstrip('\n')
                            break
                return result