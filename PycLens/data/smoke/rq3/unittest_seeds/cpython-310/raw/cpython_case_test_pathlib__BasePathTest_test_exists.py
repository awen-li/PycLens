# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_exists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE)
    self.assertIs(True, p.exists())
    self.assertIs(True, (p / 'dirA').exists())
    self.assertIs(True, (p / 'fileA').exists())
    self.assertIs(False, (p / 'fileA' / 'bah').exists())
    if os_helper.can_symlink():
        self.assertIs(True, (p / 'linkA').exists())
        self.assertIs(True, (p / 'linkB').exists())
        self.assertIs(True, (p / 'linkB' / 'fileB').exists())
        self.assertIs(False, (p / 'linkA' / 'bah').exists())
    self.assertIs(False, (p / 'foo').exists())
    self.assertIs(False, P('/xyzzy').exists())
    self.assertIs(False, P(BASE + '\udfff').exists())
    self.assertIs(False, P(BASE + '\x00').exists())
