# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_restore_signals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    default_proc_status = subprocess.check_output(['cat', '/proc/self/status'], restore_signals=False)
    for line in default_proc_status.splitlines():
        if line.startswith(b'SigIgn'):
            default_sig_ign_mask = line
            break
    else:
        self.skipTest('SigIgn not found in /proc/self/status.')
    restored_proc_status = subprocess.check_output(['cat', '/proc/self/status'], restore_signals=True)
    for line in restored_proc_status.splitlines():
        if line.startswith(b'SigIgn'):
            restored_sig_ign_mask = line
            break
    self.assertNotEqual(default_sig_ign_mask, restored_sig_ign_mask, msg="restore_signals=True should've unblocked SIGPIPE and friends.")
