# -*- coding:utf-8 -*-
import base64
import traceback
import rsa



class RSAUtils:
    MAX_ENCRYPT_BLOCK = 117
    MAX_DECRYPT_BLOCK = 128

    @classmethod
    def str_2_publickey(cls, key):
        # 对字符串解码
        b_str = base64.b64decode(key)

        if len(b_str) < 162:
            return False
        hex_str = ''
        # 按位转换成16进制
        for x in b_str:
            h = hex(ord(x))[2:]
            h = h.rjust(2, '0')
            hex_str += h

        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2
        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        return modulus,exponent

    @classmethod
    def str_2_privatekey(cls, key):
        # 对字符串解码
        b_str = base64.b64decode(key)

        if len(b_str) < 162:
            return False
        hex_str = ''
        # 按位转换成16进制
        for x in b_str:
            h = hex(ord(x))[2:]
            h = h.rjust(2, '0')
            hex_str += h
        # 找到模数和指数的开头结束位置
        m_start = 11 * 2 + 52 # 74
        m_len = 128 * 2 # 330
        e_start = 141 * 2 + 52 # 334
        e_len = 3 * 2 # 340
        d_start = 147 * 2 + 52 # 346
        d_len = 128 * 2 # 602
        p1_start = 278 * 2 + 52 # 608
        p1_len = 64 * 2 # 736
        p2_start = 345 * 2 + 52 # 742
        p2_len = 64 * 2 # 870
        exp1_start = 412 * 2 + 52 # 876
        exp1_len = 64 * 2 # 1004
        exp2_start = 478 * 2 + 52 # 1008
        exp2_len = 64 * 2 # 1136
        coe_start = 545 * 2 + 52 # 1142
        coe_len = 64 * 2 # 1270

        modulus = hex_str[m_start:m_start + m_len]
        publicexponent = hex_str[e_start:e_start + e_len]
        privateexponent = hex_str[d_start:d_start+d_len]
        prime1 = hex_str[p1_start:p1_start+p1_len]
        prime2 = hex_str[p2_start:p2_start+p2_len]
        exponent1 = hex_str[exp1_start:exp1_start + exp1_len]
        exponent2 = hex_str[exp2_start:exp2_start+exp2_len]
        coefficient = hex_str[coe_start:coe_start+coe_len]
        return modulus,publicexponent,privateexponent, prime1, prime2, exponent1, exponent2, coefficient
    
    @classmethod
    def encryptByPublicKey(cls, data, key):
        key = cls.str_2_publickey(key)
        modulus = int(key[0], 16)
        exponent = int(key[1], 16)
        rsa_pubkey = rsa.PublicKey(modulus, exponent)

        data = bytearray(data, 'utf-8')
        data = bytes(data)

        inputLen = len(data)
        offSet = 0
        out = ''
        i = 0
        while (inputLen - offSet) > 0:
            if inputLen - offSet > cls.MAX_ENCRYPT_BLOCK:
                cache = rsa.encrypt(data[offSet:offSet + cls.MAX_ENCRYPT_BLOCK], rsa_pubkey)
            else:
                cache = rsa.encrypt(data[offSet:inputLen], rsa_pubkey)
            out = out + cache
            i += 1
            offSet = i * cls.MAX_ENCRYPT_BLOCK
        out = base64.b64encode(out)
        return out

    @classmethod
    def decryptByPrivateKey(cls, data, key):
        key = cls.str_2_privatekey(key)
        modulus = int(key[0], 16)
        publicexponent = int(key[1], 16)
        privateexponent = int(key[2], 16)
        prime1 = int(key[3], 16)
        prime2 = int(key[4], 16)
        exponent1 = int(key[5], 16)
        exponent2 = int(key[6], 16)
        coefficient = int(key[7], 16)

        rsa_prikey = rsa.PrivateKey(modulus, publicexponent, privateexponent, prime1, prime2, exponent1, exponent2, coefficient)

        inputLen = len(data)
        offSet = 0
        out = ''
        i = 0
        while (inputLen - offSet) > 0:
            if inputLen - offSet > cls.MAX_DECRYPT_BLOCK:
                cache = rsa.decrypt(data[offSet:offSet + cls.MAX_DECRYPT_BLOCK], rsa_prikey)
            else:
                cache = rsa.decrypt(data[offSet:inputLen], rsa_prikey)
            out = out + cache
            i += 1
            offSet = i * cls.MAX_DECRYPT_BLOCK
        out = base64.b64encode(out)
        return out
        




if __name__== '__main__':
    r = RSAUtils()
    pub_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCa96MKLETxOgN5u2bk7z6kYYrkkjMFzEJSNNQ5bPK4klnSRN/AcyxR5mUHMUkMFeTTKkGIcckPAPIw+hveV2Ge/WFTrwazFomePmZFVxS/dQgc14q3+GXEMQ+l2w6GueWAuoQedCS6aMn/OJtC05lV8tfUe7R91AB3ba+KqKuWBwIDAQAB'
    pri_key = 'MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAJr3owosRPE6A3m7ZuTvPqRhiuSSMwXMQlI01Dls8riSWdJE38BzLFHmZQcxSQwV5NMqQYhxyQ8A8jD6G95XYZ79YVOvBrMWiZ4+ZkVXFL91CBzXirf4ZcQxD6XbDoa55YC6hB50JLpoyf84m0LTmVXy19R7tH3UAHdtr4qoq5YHAgMBAAECgYAbwf2/Rby3pNeYh3vfyAbldN9nH9Tp1fOPPA1DmANGEljqdBHMLBUlOmqgRjC6bHWHaYtBgHguKtI2+aXiRq6if2qg61XwR8V0NX2najbnJ7PpUURrZmRR2Z5C90qIKaw2hJkTaWDNbdfp9blhd4WlAuVEovXP6jrQNLcDUbSkaQJBANRDdzZhyZ2c6TLQj/3wWn1ClFsxL9Mn5v30u+GKrz1CjbOYXDb+ava1az54mjXEp3Ka4K/Q0JwLBhRW6f6jidMCQQC65eU9HMZ0omMdeFXmJLw6lrvF//mdYtg0//2W6Wlw5VPhAZwb9CgtgniYNiweaACjeSE9FUUbovTswtoXAU59AkABPmP0bZ5AziqPoak2U7I0Ca/U2PTux80Sr9xp9eYQ9dLeuoXPzK3TxDxcoVhF+GECyuWGIjMWtvnSJLA6TbsBAkBqgMtLMfSdTlQw3PwGM/TXZkIGqMGzwDn4qc/2iXg+j1BnLiWpgE7M8EaMZoJpqVaD0WjxiAdjok70BG2HIoV5AkAW166c63A2ELT/iUdam5Invt5vtel0IWRYNktMrtApu/TseoV+6p/Uht27SATnrgSiq9gFY3lOJQWVAn7NI40E'
    # data = u'hello,world !'
    # t = r.encryptByPublicKey(data, pub_key)
    # print t
    # data = "" # 加密字串
    # data = base64.b64decode(data)
    # print data
    # t = r.decryptByPrivateKey(data, pri_key)
    # print 'text' + t

    message = 'hello, world'
    t = r.encryptByPublicKey(message, pub_key)
    t = base64.b64decode(t)
    t = r.decryptByPrivateKey(t, pri_key)
    print base64.b64decode(t)