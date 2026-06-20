# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_recursive_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'1': 1, '2': 1}
    t = {'3': 3, 'd': d}
    d['t'] = t
    self.assertRaises(TypeError, xmlrpclib.dumps, (d,))
