# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFpatches_test_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    limit = sys.getrecursionlimit()
    old = [(i % 2 and 'K:%d' or 'V:A:%d') % i for i in range(limit * 2)]
    new = [(i % 2 and 'K:%d' or 'V:B:%d') % i for i in range(limit * 2)]
    difflib.SequenceMatcher(None, old, new).get_opcodes()
