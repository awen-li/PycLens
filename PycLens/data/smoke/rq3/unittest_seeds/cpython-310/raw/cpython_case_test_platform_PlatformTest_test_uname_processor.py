# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname_processor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        proc_res = subprocess.check_output(['uname', '-p'], text=True).strip()
        expect = platform._unknown_as_blank(proc_res)
    except (OSError, subprocess.CalledProcessError):
        expect = ''
    self.assertEqual(platform.uname().processor, expect)
