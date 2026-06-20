# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_type_erasure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class Node(Generic[T]):

        def __init__(self, label: T, left: 'Node[T]'=None, right: 'Node[T]'=None):
            self.label = label
            self.left = left
            self.right = right

    def foo(x: T):
        a = Node(x)
        b = Node[T](x)
        c = Node[Any](x)
        self.assertIs(type(a), Node)
        self.assertIs(type(b), Node)
        self.assertIs(type(c), Node)
        self.assertEqual(a.label, x)
        self.assertEqual(b.label, x)
        self.assertEqual(c.label, x)
    foo(42)
