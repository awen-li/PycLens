# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestExpressionStackSize_test_meth_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    kwargs = (f'a{i}=x' for i in range(self.N))
    self.check_stack_size('o.m(' + ', '.join(kwargs) + ')')
