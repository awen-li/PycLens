# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_nextfile_test_state_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nextfile_retval = object()
    instance = MockFileInput()
    instance.return_values['nextfile'] = nextfile_retval
    fileinput._state = instance
    retval = fileinput.nextfile()
    self.assertExactlyOneInvocation(instance, 'nextfile')
    self.assertIs(retval, nextfile_retval)
    self.assertIs(fileinput._state, instance)
