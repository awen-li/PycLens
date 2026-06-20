# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_close_on_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = self.writeTmp('')
    try:
        with FileInput(files=t1, encoding='utf-8') as fi:
            raise OSError
    except OSError:
        self.assertEqual(fi._files, ())
