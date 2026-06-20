# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ExhaustiveChannelTests_test_force_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (i, fix, actions) in self._iter_close_tests():
        with self.subTest('{} {}  {}'.format(i, fix, actions)):
            fix.prep_interpreter(fix.interp)
            self.run_actions(fix, actions)
            self._close(fix, force=True)
            self._assert_closed(fix)
        fix.clean_up()
