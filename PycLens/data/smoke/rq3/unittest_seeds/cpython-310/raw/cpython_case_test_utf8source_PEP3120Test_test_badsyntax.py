# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8source.py
# case: PEP3120Test_test_badsyntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import test.badsyntax_pep3120
    except SyntaxError as msg:
        msg = str(msg).lower()
        self.assertTrue('utf-8' in msg)
    else:
        self.fail("expected exception didn't occur")
