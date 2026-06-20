# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: BytecodeTests_test_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.maxDiff = 1000
    for (x, expected) in CodeInfoTests.test_pairs:
        b = dis.Bytecode(x)
        self.assertRegex(b.info(), expected)
