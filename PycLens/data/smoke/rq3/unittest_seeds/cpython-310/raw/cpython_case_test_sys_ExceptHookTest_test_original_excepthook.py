# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: ExceptHookTest_test_original_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise ValueError(42)
    except ValueError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertTrue(err.getvalue().endswith('ValueError: 42\n'))
    self.assertRaises(TypeError, sys.__excepthook__)
