# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_mro_conflicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = collections.abc

    @functools.singledispatch
    def g(arg):
        return 'base'

    class O(c.Sized):

        def __len__(self):
            return 0
    o = O()
    self.assertEqual(g(o), 'base')
    g.register(c.Iterable, lambda arg: 'iterable')
    g.register(c.Container, lambda arg: 'container')
    g.register(c.Sized, lambda arg: 'sized')
    g.register(c.Set, lambda arg: 'set')
    self.assertEqual(g(o), 'sized')
    c.Iterable.register(O)
    self.assertEqual(g(o), 'sized')
    c.Container.register(O)
    self.assertEqual(g(o), 'sized')
    c.Set.register(O)
    self.assertEqual(g(o), 'set')

    class P:
        pass
    p = P()
    self.assertEqual(g(p), 'base')
    c.Iterable.register(P)
    self.assertEqual(g(p), 'iterable')
    c.Container.register(P)
    with self.assertRaises(RuntimeError) as re_one:
        g(p)
    self.assertIn(str(re_one.exception), ("Ambiguous dispatch: <class 'collections.abc.Container'> or <class 'collections.abc.Iterable'>", "Ambiguous dispatch: <class 'collections.abc.Iterable'> or <class 'collections.abc.Container'>"))

    class Q(c.Sized):

        def __len__(self):
            return 0
    q = Q()
    self.assertEqual(g(q), 'sized')
    c.Iterable.register(Q)
    self.assertEqual(g(q), 'sized')
    c.Set.register(Q)
    self.assertEqual(g(q), 'set')

    @functools.singledispatch
    def h(arg):
        return 'base'

    @h.register(c.Sized)
    def _(arg):
        return 'sized'

    @h.register(c.Container)
    def _(arg):
        return 'container'
    with self.assertRaises(RuntimeError) as re_two:
        h(collections.defaultdict(lambda : 0))
    self.assertIn(str(re_two.exception), ("Ambiguous dispatch: <class 'collections.abc.Container'> or <class 'collections.abc.Sized'>", "Ambiguous dispatch: <class 'collections.abc.Sized'> or <class 'collections.abc.Container'>"))

    class R(collections.defaultdict):
        pass
    c.MutableSequence.register(R)

    @functools.singledispatch
    def i(arg):
        return 'base'

    @i.register(c.MutableMapping)
    def _(arg):
        return 'mapping'

    @i.register(c.MutableSequence)
    def _(arg):
        return 'sequence'
    r = R()
    self.assertEqual(i(r), 'sequence')

    class S:
        pass

    class T(S, c.Sized):

        def __len__(self):
            return 0
    t = T()
    self.assertEqual(h(t), 'sized')
    c.Container.register(T)
    self.assertEqual(h(t), 'sized')

    class U:

        def __len__(self):
            return 0
    u = U()
    self.assertEqual(h(u), 'sized')
    c.Container.register(U)
    with self.assertRaises(RuntimeError) as re_three:
        h(u)
    self.assertIn(str(re_three.exception), ("Ambiguous dispatch: <class 'collections.abc.Container'> or <class 'collections.abc.Sized'>", "Ambiguous dispatch: <class 'collections.abc.Sized'> or <class 'collections.abc.Container'>"))

    class V(c.Sized, S):

        def __len__(self):
            return 0

    @functools.singledispatch
    def j(arg):
        return 'base'

    @j.register(S)
    def _(arg):
        return 's'

    @j.register(c.Container)
    def _(arg):
        return 'container'
    v = V()
    self.assertEqual(j(v), 's')
    c.Container.register(V)
    self.assertEqual(j(v), 'container')
