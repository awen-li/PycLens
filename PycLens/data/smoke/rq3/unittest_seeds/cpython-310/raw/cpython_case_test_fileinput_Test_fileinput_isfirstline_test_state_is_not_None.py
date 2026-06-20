# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_isfirstline_test_state_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    isfirstline_retval = object()
    instance = MockFileInput()
    instance.return_values['isfirstline'] = isfirstline_retval
    fileinput._state = instance
    retval = fileinput.isfirstline()
    self.assertExactlyOneInvocation(instance, 'isfirstline')
    self.assertIs(retval, isfirstline_retval)
    self.assertIs(fileinput._state, instance)
