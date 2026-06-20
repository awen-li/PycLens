# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_line_number_implicit_return_after_async_for

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def test(aseq):
        async for i in aseq:
            body
    expected_lines = [None, 1, 2, 1]
    code_lines = [None if line is None else line - test.__code__.co_firstlineno for (_, _, line) in test.__code__.co_lines()]
    self.assertEqual(expected_lines, code_lines)
