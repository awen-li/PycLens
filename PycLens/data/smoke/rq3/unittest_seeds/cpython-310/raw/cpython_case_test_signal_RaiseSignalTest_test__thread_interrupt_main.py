# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: RaiseSignalTest_test__thread_interrupt_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n        import _thread\n        class Foo():\n            def __del__(self):\n                _thread.interrupt_main()\n\n        x = Foo()\n        '
    (rc, out, err) = assert_python_ok('-c', code)
    self.assertIn(b'OSError: Signal 2 ignored due to race condition', err)
