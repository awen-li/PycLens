# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_reduce_mutating_builtins_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    builtins_dict = builtins.__dict__
    orig = {'iter': iter, 'reversed': reversed}

    def run(builtin_name, item, sentinel=None):
        it = iter(item) if sentinel is None else iter(item, sentinel)

        class CustomStr:

            def __init__(self, name, iterator):
                self.name = name
                self.iterator = iterator

            def __hash__(self):
                return hash(self.name)

            def __eq__(self, other):
                list(self.iterator)
                return other == self.name
        del builtins_dict[builtin_name]
        builtins_dict[CustomStr(builtin_name, it)] = orig[builtin_name]
        return it.__reduce__()
    types = [(EmptyIterClass(),), (bytes(8),), (bytearray(8),), ((1, 2, 3),), (lambda : 0, 0)]
    try:
        run_iter = functools.partial(run, 'iter')
        self.assertEqual(run_iter('xyz'), (orig['iter'], ('',)))
        self.assertEqual(run_iter([1, 2, 3]), (orig['iter'], ([],)))
        self.assertEqual(run('reversed', orig['reversed'](list(range(8)))), (iter, ([],)))
        for case in types:
            self.assertEqual(run_iter(*case), (orig['iter'], ((),)))
    finally:
        for (key, func) in orig.items():
            with contextlib.suppress(KeyError):
                del builtins_dict[key]
            builtins_dict[key] = func
