# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_nested_named_except_blocks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = ''
    for i in range(12):
        code += f"{'    ' * i}try:\n"
        code += f"{'    ' * (i + 1)}raise Exception\n"
        code += f"{'    ' * i}except Exception as e:\n"
    code += f"{' ' * 4 * 12}pass"
    self._check_error(code, 'too many statically nested blocks')
