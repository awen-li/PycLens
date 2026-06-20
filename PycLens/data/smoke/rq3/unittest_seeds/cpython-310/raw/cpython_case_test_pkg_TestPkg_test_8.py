# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t8', None), ('t8 __init__' + os.extsep + 'py', "'doc for t8'")]
    self.mkhier(hier)
    import t8
    self.assertEqual(t8.__doc__, 'doc for t8')
