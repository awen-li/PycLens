# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for expected in range(6):
        data = dict.fromkeys('abcde'[:expected])
        self.assertEqual(len(data), expected)
        view = self.mappingproxy(data)
        self.assertEqual(len(view), expected)
