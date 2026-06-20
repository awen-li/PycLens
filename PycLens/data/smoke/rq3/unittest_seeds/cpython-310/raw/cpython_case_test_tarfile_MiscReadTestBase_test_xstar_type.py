# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_xstar_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.tar.getmember('misc/regtype-xstar')
    except KeyError:
        self.fail('failed to find misc/regtype-xstar (mangled prefix?)')
