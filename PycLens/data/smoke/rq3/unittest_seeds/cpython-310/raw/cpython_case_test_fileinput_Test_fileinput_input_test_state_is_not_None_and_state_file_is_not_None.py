# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_fileinput_input_test_state_is_not_None_and_state_file_is_not_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    instance = MockFileInput()
    instance._file = object()
    fileinput._state = instance
    with self.assertRaises(RuntimeError) as cm:
        fileinput.input()
    self.assertEqual(('input() already active',), cm.exception.args)
    self.assertIs(instance, fileinput._state, 'fileinput._state')
