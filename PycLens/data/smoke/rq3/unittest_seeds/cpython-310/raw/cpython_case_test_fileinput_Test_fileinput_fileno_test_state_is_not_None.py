# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_fileno_test_state_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileno_retval = object()
    instance = MockFileInput()
    instance.return_values['fileno'] = fileno_retval
    instance.fileno_retval = fileno_retval
    fileinput._state = instance
    retval = fileinput.fileno()
    self.assertExactlyOneInvocation(instance, 'fileno')
    self.assertIs(retval, fileno_retval)
    self.assertIs(fileinput._state, instance)
