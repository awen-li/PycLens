# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_print.py
# case: TestPy2MigrationHint_test_stream_redirection_hint_for_py2_migration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError) as context:
        (print >> sys.stderr, 'message')
    self.assertIn('Did you mean "print(<message>, file=<output_stream>)"?', str(context.exception))
    with self.assertRaises(TypeError) as context:
        print >> 42
    self.assertIn('Did you mean "print(<message>, file=<output_stream>)"?', str(context.exception))
    with self.assertRaises(TypeError) as context:
        max >> sys.stderr
    self.assertNotIn('Did you mean ', str(context.exception))
    with self.assertRaises(TypeError) as context:
        print << sys.stderr
    self.assertNotIn('Did you mean', str(context.exception))

    class OverrideRRShift:

        def __rrshift__(self, lhs):
            return 42
    self.assertEqual(print >> OverrideRRShift(), 42)
