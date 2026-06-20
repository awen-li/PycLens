# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestBreakpoint_test_envar_good_path_noop_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.env['PYTHONBREAKPOINT'] = '0'
    with patch('pdb.set_trace') as mock:
        breakpoint()
        mock.assert_not_called()
