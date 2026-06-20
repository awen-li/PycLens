# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_walk_packages_raises_on_string_or_bytes_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_input = 'test_dir'
    with self.assertRaises((TypeError, ValueError)):
        list(pkgutil.walk_packages(str_input))
    bytes_input = b'test_dir'
    with self.assertRaises((TypeError, ValueError)):
        list(pkgutil.walk_packages(bytes_input))
