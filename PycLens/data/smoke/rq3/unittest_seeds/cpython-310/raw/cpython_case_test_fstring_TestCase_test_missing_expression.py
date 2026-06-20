# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_missing_expression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(SyntaxError, 'f-string: empty expression not allowed', ["f'{}'", "f'{ }'f' {} '", "f'{!r}'", "f'{ !r}'", "f'{10:{ }}'", "f' { } '", "f'''{\t\x0c\r\n}'''", "f'{!x}'", "f'{ !xr}'", "f'{!x:}'", "f'{!x:a}'", "f'{ !xr:}'", "f'{ !xr:a}'", "f'{!}'", "f'{:}'", "f'{!'", "f'{!s:'", "f'{:'", "f'{:x'"])
    self.assertAllRaise(SyntaxError, 'invalid non-printable character U\\+00A0', ["f'''{\xa0}'''", '\xa0'])
