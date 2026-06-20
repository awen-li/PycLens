# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_suites

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            while True:\n                pass\n\n            if one():\n                x = None\n            elif other():\n                y = None\n            else:\n                z = None\n\n            for x, y in stuff:\n                assert True\n\n            try:\n                raise RuntimeError\n            except TypeError as e:\n                pass\n\n            pass\n        ').strip()
    mod = ast.parse(s)
    while_loop = mod.body[0]
    if_stmt = mod.body[1]
    for_loop = mod.body[2]
    try_stmt = mod.body[3]
    pass_stmt = mod.body[4]
    self._check_end_pos(while_loop, 2, 8)
    self._check_end_pos(if_stmt, 9, 12)
    self._check_end_pos(for_loop, 12, 15)
    self._check_end_pos(try_stmt, 17, 8)
    self._check_end_pos(pass_stmt, 19, 4)
    self._check_content(s, while_loop.test, 'True')
    self._check_content(s, if_stmt.body[0], 'x = None')
    self._check_content(s, if_stmt.orelse[0].test, 'other()')
    self._check_content(s, for_loop.target, 'x, y')
    self._check_content(s, try_stmt.body[0], 'raise RuntimeError')
    self._check_content(s, try_stmt.handlers[0].type, 'TypeError')
