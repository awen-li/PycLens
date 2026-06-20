# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: ChecklineTests_test_checkline_before_debugging

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'w') as f:
        f.write('print(123)')
    db = pdb.Pdb()
    self.assertEqual(db.checkline(os_helper.TESTFN, 1), 1)
