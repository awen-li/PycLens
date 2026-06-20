# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PathTConverterTests_test_path_t_converter_and_custom_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '__fspath__\\(\\) to return str or bytes, not %s'
    with self.assertRaisesRegex(TypeError, msg % 'int'):
        os.stat(FakePath(2))
    with self.assertRaisesRegex(TypeError, msg % 'float'):
        os.stat(FakePath(2.34))
    with self.assertRaisesRegex(TypeError, msg % 'object'):
        os.stat(FakePath(object()))
