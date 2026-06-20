# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_fileno_when_ValueError_raised

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class FilenoRaisesValueError(UnconditionallyRaise):

        def __init__(self):
            UnconditionallyRaise.__init__(self, ValueError)

        def fileno(self):
            self.__call__()
    unconditionally_raise_ValueError = FilenoRaisesValueError()
    t = self.writeTmp('\n')
    with FileInput(files=[t], encoding='utf-8') as fi:
        file_backup = fi._file
        try:
            fi._file = unconditionally_raise_ValueError
            result = fi.fileno()
        finally:
            fi._file = file_backup
    self.assertTrue(unconditionally_raise_ValueError.invoked, '_file.fileno() was not invoked')
    self.assertEqual(result, -1, 'fileno() should return -1')
