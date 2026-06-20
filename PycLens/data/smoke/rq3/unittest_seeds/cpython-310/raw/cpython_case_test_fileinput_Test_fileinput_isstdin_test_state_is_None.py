# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_isstdin_test_state_is_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileinput._state = None
    with self.assertRaises(RuntimeError) as cm:
        fileinput.isstdin()
    self.assertEqual(('no active input()',), cm.exception.args)
    self.assertIsNone(fileinput._state)
