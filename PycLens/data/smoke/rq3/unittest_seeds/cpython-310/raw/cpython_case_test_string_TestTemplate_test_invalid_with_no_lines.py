# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_invalid_with_no_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyTemplate(Template):
        pattern = '\n              (?P<invalid>) |\n              unreachable(\n                (?P<named>)   |\n                (?P<braced>)  |\n                (?P<escaped>)\n              )\n            '
    s = MyTemplate('')
    with self.assertRaises(ValueError) as err:
        s.substitute({})
    self.assertIn('line 1, col 1', str(err.exception))
