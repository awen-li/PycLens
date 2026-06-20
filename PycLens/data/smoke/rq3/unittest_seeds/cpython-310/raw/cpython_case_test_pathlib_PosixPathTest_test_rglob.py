# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_rglob

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE, 'dirC')
    given = set(p.rglob('FILEd'))
    expect = set() if not os_helper.fs_is_case_insensitive(BASE) else given
    self.assertEqual(given, expect)
    self.assertEqual(set(p.rglob('FILEd*')), set())
