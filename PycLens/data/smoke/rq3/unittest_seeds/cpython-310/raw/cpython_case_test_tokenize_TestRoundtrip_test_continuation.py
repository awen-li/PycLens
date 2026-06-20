# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestRoundtrip_test_continuation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_roundtrip("a = (3,4, \n5,6)\ny = [3, 4,\n5]\nz = {'a': 5,\n'b':15, 'c':True}\nx = len(y) + 5 - a[\n3] - a[2]\n+ len(z) - z[\n'b']\n")
