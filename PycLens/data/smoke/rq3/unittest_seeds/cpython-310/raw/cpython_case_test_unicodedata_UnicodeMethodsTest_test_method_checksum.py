# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMethodsTest_test_method_checksum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = hashlib.sha1()
    for i in range(sys.maxunicode + 1):
        char = chr(i)
        data = ['01'[char.isalnum()], '01'[char.isalpha()], '01'[char.isdecimal()], '01'[char.isdigit()], '01'[char.islower()], '01'[char.isnumeric()], '01'[char.isspace()], '01'[char.istitle()], '01'[char.isupper()], '01'[(char + 'abc').isalnum()], '01'[(char + 'abc').isalpha()], '01'[(char + '123').isdecimal()], '01'[(char + '123').isdigit()], '01'[(char + 'abc').islower()], '01'[(char + '123').isnumeric()], '01'[(char + ' \t').isspace()], '01'[(char + 'abc').istitle()], '01'[(char + 'ABC').isupper()], char.lower(), char.upper(), char.title(), (char + 'abc').lower(), (char + 'ABC').upper(), (char + 'abc').title(), (char + 'ABC').title()]
        h.update(''.join(data).encode('utf-8', 'surrogatepass'))
    result = h.hexdigest()
    self.assertEqual(result, self.expectedchecksum)
