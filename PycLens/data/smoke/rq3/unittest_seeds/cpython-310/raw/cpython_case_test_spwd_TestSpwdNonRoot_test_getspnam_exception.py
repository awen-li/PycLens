# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_spwd.py
# case: TestSpwdNonRoot_test_getspnam_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'bin'
    try:
        with self.assertRaises(PermissionError) as cm:
            spwd.getspnam(name)
    except KeyError as exc:
        self.skipTest("spwd entry %r doesn't exist: %s" % (name, exc))
