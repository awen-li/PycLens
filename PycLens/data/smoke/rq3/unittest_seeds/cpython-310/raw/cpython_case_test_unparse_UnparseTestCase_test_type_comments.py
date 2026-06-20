# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_type_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for statement in ('a = 5 # type:', 'a = 5 # type: int', 'a = 5 # type: int and more', 'def x(): # type: () -> None\n\tpass', 'def x(y): # type: (int) -> None and more\n\tpass', 'async def x(): # type: () -> None\n\tpass', 'async def x(y): # type: (int) -> None and more\n\tpass', 'for x in y: # type: int\n\tpass', 'async for x in y: # type: int\n\tpass', 'with x(): # type: int\n\tpass', 'async with x(): # type: int\n\tpass'):
        self.check_ast_roundtrip(statement, type_comments=True)
