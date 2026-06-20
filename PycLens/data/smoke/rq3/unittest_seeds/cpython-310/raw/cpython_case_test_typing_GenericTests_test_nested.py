# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    G = Generic

    class Visitor(G[T]):
        a = None

        def set(self, a: T):
            self.a = a

        def get(self):
            return self.a

        def visit(self) -> T:
            return self.a
    V = Visitor[typing.List[int]]

    class IntListVisitor(V):

        def append(self, x: int):
            self.a.append(x)
    a = IntListVisitor()
    a.set([])
    a.append(1)
    a.append(42)
    self.assertEqual(a.get(), [1, 42])
