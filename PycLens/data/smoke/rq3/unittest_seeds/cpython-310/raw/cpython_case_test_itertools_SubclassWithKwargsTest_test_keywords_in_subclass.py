# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: SubclassWithKwargsTest_test_keywords_in_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cls in (repeat, zip, filter, filterfalse, chain, map, starmap, islice, takewhile, dropwhile, cycle, compress):

        class Subclass(cls):

            def __init__(self, newarg=None, *args):
                cls.__init__(self, *args)
        try:
            Subclass(newarg=1)
        except TypeError as err:
            self.assertNotIn('keyword arguments', err.args[0])
