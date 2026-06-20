# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test__getitem__eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.writeTmp('')
    with FileInput(files=[t], encoding='utf-8') as fi:
        with self.assertRaises(IndexError) as cm:
            fi[0]
    self.assertEqual(cm.exception.args, ('end of input reached',))
