# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class manager(object):

        def __enter__(self):
            return (1, 2)

        def __exit__(self, *args):
            pass
    with manager():
        pass
    with manager() as x:
        pass
    with manager() as (x, y):
        pass
    with manager(), manager():
        pass
    with manager() as x, manager() as y:
        pass
    with manager() as x, manager():
        pass
    with manager():
        pass
    with manager() as x:
        pass
    with manager() as (x, y), manager() as z:
        pass
    with manager(), manager():
        pass
    with manager() as x, manager() as y:
        pass
    with manager() as x, manager():
        pass
    with manager() as x, manager() as y, manager() as z:
        pass
    with manager() as x, manager() as y, manager():
        pass
