# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_huntrleaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            GLOBAL_LIST = []\n\n            class RefLeakTest(unittest.TestCase):\n                def test_leak(self):\n                    GLOBAL_LIST.append(object())\n        ')
    self.check_leak(code, 'references')
