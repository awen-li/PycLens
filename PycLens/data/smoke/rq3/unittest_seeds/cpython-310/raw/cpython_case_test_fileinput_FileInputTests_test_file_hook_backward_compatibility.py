# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_file_hook_backward_compatibility

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def old_hook(filename, mode):
        return io.StringIO('I used to receive only filename and mode')
    t = self.writeTmp('\n')
    with FileInput([t], openhook=old_hook) as fi:
        result = fi.readline()
    self.assertEqual(result, 'I used to receive only filename and mode')
