# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_lineno_procedure_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def call():
        print()
    line1 = call.__code__.co_firstlineno + 1
    assert line1 not in [line for (_, _, line) in call.__code__.co_lines()]
