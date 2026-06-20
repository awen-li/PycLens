# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_logging_at_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import logging\n\n            class A:\n                def __del__(self):\n                    try:\n                        raise ValueError("some error")\n                    except Exception:\n                        logging.exception("exception in __del__")\n\n            a = A()\n        ')
    (rc, out, err) = assert_python_ok('-c', code)
    err = err.decode()
    self.assertIn('exception in __del__', err)
    self.assertIn('ValueError: some error', err)
