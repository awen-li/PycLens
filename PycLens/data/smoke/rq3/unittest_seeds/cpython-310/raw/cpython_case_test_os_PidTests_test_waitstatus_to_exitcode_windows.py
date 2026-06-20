# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PidTests_test_waitstatus_to_exitcode_windows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    max_exitcode = 2 ** 32 - 1
    for exitcode in (0, 1, 5, max_exitcode):
        self.assertEqual(os.waitstatus_to_exitcode(exitcode << 8), exitcode)
    with self.assertRaises(ValueError):
        os.waitstatus_to_exitcode(max_exitcode + 1 << 8)
    with self.assertRaises(OverflowError):
        os.waitstatus_to_exitcode(-1)
