# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_line_number_genexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def return_genexp():
        return (1 for x in y)
    genexp_lines = [None, 1, 3, 1]
    genexp_code = return_genexp.__code__.co_consts[1]
    code_lines = [None if line is None else line - return_genexp.__code__.co_firstlineno for (_, _, line) in genexp_code.co_lines()]
    self.assertEqual(genexp_lines, code_lines)
