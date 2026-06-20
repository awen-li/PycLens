# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_truncate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxlen = 500
    func_name = 'x' * (maxlen + 50)
    truncated = 'x' * maxlen + '...'
    code = '\n            import faulthandler\n\n            def {func_name}():\n                faulthandler.dump_traceback(all_threads=False)\n\n            {func_name}()\n            '
    code = code.format(func_name=func_name)
    expected = ['Stack (most recent call first):', '  File "<string>", line 4 in %s' % truncated, '  File "<string>", line 6 in <module>']
    (trace, exitcode) = self.get_output(code)
    self.assertEqual(trace, expected)
    self.assertEqual(exitcode, 0)
