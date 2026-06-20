# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestBreakpoint_test_envar_unimportable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for envar in ('.', '..', '.foo', 'foo.', '.int', 'int.', '.foo.bar', '..foo.bar', '/./', 'nosuchbuiltin', 'nosuchmodule.nosuchcallable'):
        with self.subTest(envar=envar):
            self.env['PYTHONBREAKPOINT'] = envar
            mock = self.resources.enter_context(patch('pdb.set_trace'))
            w = self.resources.enter_context(check_warnings(quiet=True))
            breakpoint()
            self.assertEqual(str(w.message), f'Ignoring unimportable $PYTHONBREAKPOINT: "{envar}"')
            self.assertEqual(w.category, RuntimeWarning)
            mock.assert_not_called()
