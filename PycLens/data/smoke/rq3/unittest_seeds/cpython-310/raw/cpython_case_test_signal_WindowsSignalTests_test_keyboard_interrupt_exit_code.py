# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WindowsSignalTests_test_keyboard_interrupt_exit_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    process = subprocess.run([sys.executable, '-c', 'raise KeyboardInterrupt'], stderr=subprocess.PIPE)
    self.assertIn(b'KeyboardInterrupt', process.stderr)
    STATUS_CONTROL_C_EXIT = 3221225786
    self.assertEqual(process.returncode, STATUS_CONTROL_C_EXIT)
