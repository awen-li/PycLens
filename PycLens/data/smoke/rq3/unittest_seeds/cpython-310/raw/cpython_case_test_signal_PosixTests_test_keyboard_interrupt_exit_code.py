# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_keyboard_interrupt_exit_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    process = subprocess.run([sys.executable, '-c', 'import os, signal, time\nos.kill(os.getpid(), signal.SIGINT)\nfor _ in range(999): time.sleep(0.01)'], stderr=subprocess.PIPE)
    self.assertIn(b'KeyboardInterrupt', process.stderr)
    self.assertEqual(process.returncode, -signal.SIGINT)
