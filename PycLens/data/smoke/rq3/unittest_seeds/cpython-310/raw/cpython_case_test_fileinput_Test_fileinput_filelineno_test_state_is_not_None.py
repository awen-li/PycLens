# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_filelineno_test_state_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filelineno_retval = object()
    instance = MockFileInput()
    instance.return_values['filelineno'] = filelineno_retval
    fileinput._state = instance
    retval = fileinput.filelineno()
    self.assertExactlyOneInvocation(instance, 'filelineno')
    self.assertIs(retval, filelineno_retval)
    self.assertIs(fileinput._state, instance)
