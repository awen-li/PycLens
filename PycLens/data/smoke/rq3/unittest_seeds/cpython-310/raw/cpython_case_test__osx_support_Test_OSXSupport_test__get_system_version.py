# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__get_system_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(platform.mac_ver()[0].startswith(_osx_support._get_system_version()))
