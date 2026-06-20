# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_empty_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "from enum import Enum; Enum('Animal', 'ANT BEE CAT DOG')"
    code = compile(code, '<string>', 'exec')
    global_ns = {}
    local_ls = {}
    exec(code, global_ns, local_ls)
