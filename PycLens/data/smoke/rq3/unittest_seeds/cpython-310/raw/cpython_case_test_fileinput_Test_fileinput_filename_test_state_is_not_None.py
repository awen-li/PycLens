# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_filename_test_state_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename_retval = object()
    instance = MockFileInput()
    instance.return_values['filename'] = filename_retval
    fileinput._state = instance
    retval = fileinput.filename()
    self.assertExactlyOneInvocation(instance, 'filename')
    self.assertIs(retval, filename_retval)
    self.assertIs(fileinput._state, instance)
