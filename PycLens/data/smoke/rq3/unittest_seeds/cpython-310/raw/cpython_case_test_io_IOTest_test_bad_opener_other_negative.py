# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_bad_opener_other_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def badopener(fname, flags):
        return -2
    with self.assertRaises(ValueError) as cm:
        open('non-existent', 'r', opener=badopener)
    self.assertEqual(str(cm.exception), 'opener returned -2')
