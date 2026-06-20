# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegator_is_visible_to_debugger

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def call_stack():
        return [f[3] for f in inspect.stack()]

    def gen():
        yield call_stack()
        yield call_stack()
        yield call_stack()

    def spam(g):
        yield from g

    def eggs(g):
        yield from g
    for stack in spam(gen()):
        self.assertTrue('spam' in stack)
    for stack in spam(eggs(gen())):
        self.assertTrue('spam' in stack and 'eggs' in stack)
