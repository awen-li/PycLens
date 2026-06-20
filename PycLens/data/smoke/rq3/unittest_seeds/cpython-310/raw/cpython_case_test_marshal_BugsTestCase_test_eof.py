# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = marshal.dumps(('hello', 'dolly', None))
    for i in range(len(data)):
        self.assertRaises(EOFError, marshal.loads, data[0:i])
