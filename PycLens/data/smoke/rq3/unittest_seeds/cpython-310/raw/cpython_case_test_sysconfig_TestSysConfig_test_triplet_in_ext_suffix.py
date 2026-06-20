# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_triplet_in_ext_suffix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctypes = import_module('ctypes')
    import platform, re
    machine = platform.machine()
    suffix = sysconfig.get_config_var('EXT_SUFFIX')
    if re.match('(aarch64|arm|mips|ppc|powerpc|s390|sparc)', machine):
        self.assertTrue('linux' in suffix, suffix)
    if re.match('(i[3-6]86|x86_64)$', machine):
        if ctypes.sizeof(ctypes.c_char_p()) == 4:
            self.assertTrue(suffix.endswith('i386-linux-gnu.so') or suffix.endswith('x86_64-linux-gnux32.so'), suffix)
        else:
            self.assertTrue(suffix.endswith('x86_64-linux-gnu.so'), suffix)
