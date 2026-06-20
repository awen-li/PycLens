# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: CodeInfoTests_test_code_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.maxDiff = 1000
    for (x, expected) in self.test_pairs:
        self.assertRegex(dis.code_info(x), expected)
