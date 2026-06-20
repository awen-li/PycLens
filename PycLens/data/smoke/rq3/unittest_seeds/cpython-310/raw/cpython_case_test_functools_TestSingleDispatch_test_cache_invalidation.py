# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_cache_invalidation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from collections import UserDict
    import weakref

    class TracingDict(UserDict):

        def __init__(self, *args, **kwargs):
            super(TracingDict, self).__init__(*args, **kwargs)
            self.set_ops = []
            self.get_ops = []

        def __getitem__(self, key):
            result = self.data[key]
            self.get_ops.append(key)
            return result

        def __setitem__(self, key, value):
            self.set_ops.append(key)
            self.data[key] = value

        def clear(self):
            self.data.clear()
    td = TracingDict()
    with support.swap_attr(weakref, 'WeakKeyDictionary', lambda : td):
        c = collections.abc

        @functools.singledispatch
        def g(arg):
            return 'base'
        d = {}
        l = []
        self.assertEqual(len(td), 0)
        self.assertEqual(g(d), 'base')
        self.assertEqual(len(td), 1)
        self.assertEqual(td.get_ops, [])
        self.assertEqual(td.set_ops, [dict])
        self.assertEqual(td.data[dict], g.registry[object])
        self.assertEqual(g(l), 'base')
        self.assertEqual(len(td), 2)
        self.assertEqual(td.get_ops, [])
        self.assertEqual(td.set_ops, [dict, list])
        self.assertEqual(td.data[dict], g.registry[object])
        self.assertEqual(td.data[list], g.registry[object])
        self.assertEqual(td.data[dict], td.data[list])
        self.assertEqual(g(l), 'base')
        self.assertEqual(g(d), 'base')
        self.assertEqual(td.get_ops, [list, dict])
        self.assertEqual(td.set_ops, [dict, list])
        g.register(list, lambda arg: 'list')
        self.assertEqual(td.get_ops, [list, dict])
        self.assertEqual(len(td), 0)
        self.assertEqual(g(d), 'base')
        self.assertEqual(len(td), 1)
        self.assertEqual(td.get_ops, [list, dict])
        self.assertEqual(td.set_ops, [dict, list, dict])
        self.assertEqual(td.data[dict], functools._find_impl(dict, g.registry))
        self.assertEqual(g(l), 'list')
        self.assertEqual(len(td), 2)
        self.assertEqual(td.get_ops, [list, dict])
        self.assertEqual(td.set_ops, [dict, list, dict, list])
        self.assertEqual(td.data[list], functools._find_impl(list, g.registry))

        class X:
            pass
        c.MutableMapping.register(X)
        self.assertEqual(g(d), 'base')
        self.assertEqual(g(l), 'list')
        self.assertEqual(td.get_ops, [list, dict, dict, list])
        self.assertEqual(td.set_ops, [dict, list, dict, list])
        g.register(c.Sized, lambda arg: 'sized')
        self.assertEqual(len(td), 0)
        self.assertEqual(g(d), 'sized')
        self.assertEqual(len(td), 1)
        self.assertEqual(td.get_ops, [list, dict, dict, list])
        self.assertEqual(td.set_ops, [dict, list, dict, list, dict])
        self.assertEqual(g(l), 'list')
        self.assertEqual(len(td), 2)
        self.assertEqual(td.get_ops, [list, dict, dict, list])
        self.assertEqual(td.set_ops, [dict, list, dict, list, dict, list])
        self.assertEqual(g(l), 'list')
        self.assertEqual(g(d), 'sized')
        self.assertEqual(td.get_ops, [list, dict, dict, list, list, dict])
        self.assertEqual(td.set_ops, [dict, list, dict, list, dict, list])
        g.dispatch(list)
        g.dispatch(dict)
        self.assertEqual(td.get_ops, [list, dict, dict, list, list, dict, list, dict])
        self.assertEqual(td.set_ops, [dict, list, dict, list, dict, list])
        c.MutableSet.register(X)
        self.assertEqual(len(td), 2)
        self.assertEqual(g(l), 'list')
        self.assertEqual(len(td), 1)
        g.register(c.MutableMapping, lambda arg: 'mutablemapping')
        self.assertEqual(len(td), 0)
        self.assertEqual(g(d), 'mutablemapping')
        self.assertEqual(len(td), 1)
        self.assertEqual(g(l), 'list')
        self.assertEqual(len(td), 2)
        g.register(dict, lambda arg: 'dict')
        self.assertEqual(g(d), 'dict')
        self.assertEqual(g(l), 'list')
        g._clear_cache()
        self.assertEqual(len(td), 0)
