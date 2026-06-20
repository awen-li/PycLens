# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: FinalizeTestCase_test_atexit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prog = 'from test.test_weakref import FinalizeTestCase;' + 'FinalizeTestCase.run_in_child()'
    (rc, out, err) = script_helper.assert_python_ok('-c', prog)
    out = out.decode('ascii').splitlines()
    self.assertEqual(out, ['f4 foobar', 'f3 error', 'g1', 'f1 foobar'])
    self.assertTrue(b'ZeroDivisionError' in err)
