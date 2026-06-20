# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_format_exception_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = Exception('projector')
    output = traceback.format_exception(e)
    self.assertEqual(output, ['Exception: projector\n'])
    with self.assertRaisesRegex(ValueError, 'Both or neither'):
        traceback.format_exception(e.__class__, e)
    with self.assertRaisesRegex(ValueError, 'Both or neither'):
        traceback.format_exception(e.__class__, tb=e.__traceback__)
    with self.assertRaisesRegex(TypeError, 'positional-only'):
        traceback.format_exception(exc=e)
