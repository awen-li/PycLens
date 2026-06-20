# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        imghdr.what()
    with self.assertRaises(AttributeError):
        imghdr.what(None)
    with self.assertRaises(TypeError):
        imghdr.what(self.testfile, 1)
    with self.assertRaises(AttributeError):
        imghdr.what(os.fsencode(self.testfile))
    with open(self.testfile, 'rb') as f:
        with self.assertRaises(AttributeError):
            imghdr.what(f.fileno())
