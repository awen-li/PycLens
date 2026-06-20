# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_type_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for statement in ('a = 5 # type: ignore', 'a = 5 # type: ignore and more', 'def x(): # type: ignore\n\tpass', 'def x(y): # type: ignore and more\n\tpass', 'async def x(): # type: ignore\n\tpass', 'async def x(y): # type: ignore and more\n\tpass', 'for x in y: # type: ignore\n\tpass', 'async for x in y: # type: ignore\n\tpass', 'with x(): # type: ignore\n\tpass', 'async with x(): # type: ignore\n\tpass'):
        self.check_ast_roundtrip(statement, type_comments=True)
