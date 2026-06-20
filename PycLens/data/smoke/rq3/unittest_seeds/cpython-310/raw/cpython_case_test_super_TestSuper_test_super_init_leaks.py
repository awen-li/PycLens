# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_super_init_leaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sp = super(float, 1.0)
    for i in range(1000):
        super.__init__(sp, int, i)
