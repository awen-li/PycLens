# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_issue2301

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        compile(b"# coding: cp932\nprint '\x94N'", 'dummy', 'exec')
    except SyntaxError as v:
        self.assertEqual(v.text.rstrip('\n'), "print '年'")
    else:
        self.fail()
