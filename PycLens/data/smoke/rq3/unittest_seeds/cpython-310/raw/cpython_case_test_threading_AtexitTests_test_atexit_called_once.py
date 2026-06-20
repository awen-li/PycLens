# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: AtexitTests_test_atexit_called_once

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            import threading\n            from unittest.mock import Mock\n\n            mock = Mock()\n            threading._register_atexit(mock)\n            mock.assert_not_called()\n            # force early shutdown to ensure it was called once\n            threading._shutdown()\n            mock.assert_called_once()\n        ')
    self.assertFalse(err)
