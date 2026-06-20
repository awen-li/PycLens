# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_fstring_multi_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            f"""Some multi-line text.\n            {\n            arg_one\n            +\n            arg_two\n            }\n            It goes on..."""\n        ').strip()
    fstr = self._parse_value(s)
    binop = fstr.values[1].value
    self._check_end_pos(binop, 5, 7)
    self._check_content(s, binop.left, 'arg_one')
    self._check_content(s, binop.right, 'arg_two')
