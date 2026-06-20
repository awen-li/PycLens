# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_load_standard_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_loads
    check('string', 'string')
    check('<string>string</string>', 'string')
    check('<string>𝔘𝔫𝔦𝔠𝔬𝔡𝔢 string</string>', '𝔘𝔫𝔦𝔠𝔬𝔡𝔢 string')
    check('<int>2056183947</int>', 2056183947)
    check('<int>-2056183947</int>', -2056183947)
    check('<i4>2056183947</i4>', 2056183947)
    check('<double>46093.78125</double>', 46093.78125)
    check('<boolean>0</boolean>', False)
    check('<base64>AGJ5dGUgc3RyaW5n/w==</base64>', xmlrpclib.Binary(b'\x00byte string\xff'))
    check('<base64>AGJ5dGUgc3RyaW5n/w==</base64>', b'\x00byte string\xff', use_builtin_types=True)
    check('<dateTime.iso8601>20050210T11:41:23</dateTime.iso8601>', xmlrpclib.DateTime('20050210T11:41:23'))
    check('<dateTime.iso8601>20050210T11:41:23</dateTime.iso8601>', datetime.datetime(2005, 2, 10, 11, 41, 23), use_builtin_types=True)
    check('<array><data><value><int>1</int></value><value><int>2</int></value></data></array>', [1, 2])
    check('<struct><member><name>b</name><value><int>2</int></value></member><member><name>a</name><value><int>1</int></value></member></struct>', {'a': 1, 'b': 2})
