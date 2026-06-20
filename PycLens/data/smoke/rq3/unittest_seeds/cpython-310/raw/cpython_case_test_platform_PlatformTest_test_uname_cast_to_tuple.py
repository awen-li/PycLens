# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname_cast_to_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = platform.uname()
    expected = (res.system, res.node, res.release, res.version, res.machine, res.processor)
    self.assertEqual(tuple(res), expected)
