# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__supports_universal_builds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import platform
    mac_ver_tuple = tuple((int(i) for i in platform.mac_ver()[0].split('.')[0:2]))
    self.assertEqual(mac_ver_tuple >= (10, 4), _osx_support._supports_universal_builds())
