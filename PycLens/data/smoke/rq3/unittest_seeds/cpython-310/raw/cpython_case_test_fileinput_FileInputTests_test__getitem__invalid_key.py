# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test__getitem__invalid_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.writeTmp('line1\nline2\n')
    with FileInput(files=[t], encoding='utf-8') as fi:
        with self.assertRaises(RuntimeError) as cm:
            fi[1]
    self.assertEqual(cm.exception.args, ('accessing lines out of order',))
