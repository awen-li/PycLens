# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_missing_format_spec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class O:

        def __format__(self, spec):
            if not spec:
                return '*'
            return spec
    self.assertEqual(f'{O():x}', 'x')
    self.assertEqual(f'{O()}', '*')
    self.assertEqual(f'{O():}', '*')
    self.assertEqual(f'{3:}', '3')
    self.assertEqual(f'{3!s:}', '3')
