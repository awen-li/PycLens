# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_func_def

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            def func(x: int,\n                     *args: str,\n                     z: float = 0,\n                     **kwargs: Any) -> bool:\n                return True\n            ').strip()
    fdef = ast.parse(s).body[0]
    self._check_end_pos(fdef, 5, 15)
    self._check_content(s, fdef.body[0], 'return True')
    self._check_content(s, fdef.args.args[0], 'x: int')
    self._check_content(s, fdef.args.args[0].annotation, 'int')
    self._check_content(s, fdef.args.kwarg, 'kwargs: Any')
    self._check_content(s, fdef.args.kwarg.annotation, 'Any')
