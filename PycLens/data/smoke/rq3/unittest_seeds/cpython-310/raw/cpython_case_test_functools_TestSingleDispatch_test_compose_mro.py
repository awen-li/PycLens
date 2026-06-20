# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_compose_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = collections.abc
    mro = functools._compose_mro
    bases = [c.Sequence, c.MutableMapping, c.Mapping, c.Set]
    for haystack in permutations(bases):
        m = mro(dict, haystack)
        self.assertEqual(m, [dict, c.MutableMapping, c.Mapping, c.Collection, c.Sized, c.Iterable, c.Container, object])
    bases = [c.Container, c.Mapping, c.MutableMapping, collections.OrderedDict]
    for haystack in permutations(bases):
        m = mro(collections.ChainMap, haystack)
        self.assertEqual(m, [collections.ChainMap, c.MutableMapping, c.Mapping, c.Collection, c.Sized, c.Iterable, c.Container, object])
    bases = [c.Container, c.Sized, str]
    for haystack in permutations(bases):
        m = mro(collections.defaultdict, [c.Sized, c.Container, str])
        self.assertEqual(m, [collections.defaultdict, dict, c.Sized, c.Container, object])

    class D(collections.defaultdict):
        pass
    c.MutableSequence.register(D)
    bases = [c.MutableSequence, c.MutableMapping]
    for haystack in permutations(bases):
        m = mro(D, bases)
        self.assertEqual(m, [D, c.MutableSequence, c.Sequence, c.Reversible, collections.defaultdict, dict, c.MutableMapping, c.Mapping, c.Collection, c.Sized, c.Iterable, c.Container, object])

    class C(collections.defaultdict):

        def __call__(self):
            pass
    bases = [c.Sized, c.Callable, c.Container, c.Mapping]
    for haystack in permutations(bases):
        m = mro(C, haystack)
        self.assertEqual(m, [C, c.Callable, collections.defaultdict, dict, c.Mapping, c.Collection, c.Sized, c.Iterable, c.Container, object])
