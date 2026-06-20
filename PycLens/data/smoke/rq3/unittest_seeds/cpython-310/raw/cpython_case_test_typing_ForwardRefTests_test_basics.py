# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Node(Generic[T]):

        def __init__(self, label: T):
            self.label = label
            self.left = self.right = None

        def add_both(self, left: 'Optional[Node[T]]', right: 'Node[T]'=None, stuff: int=None, blah=None):
            self.left = left
            self.right = right

        def add_left(self, node: Optional['Node[T]']):
            self.add_both(node, None)

        def add_right(self, node: 'Node[T]'=None):
            self.add_both(None, node)
    t = Node[int]
    both_hints = get_type_hints(t.add_both, globals(), locals())
    self.assertEqual(both_hints['left'], Optional[Node[T]])
    self.assertEqual(both_hints['right'], Optional[Node[T]])
    self.assertEqual(both_hints['left'], both_hints['right'])
    self.assertEqual(both_hints['stuff'], Optional[int])
    self.assertNotIn('blah', both_hints)
    left_hints = get_type_hints(t.add_left, globals(), locals())
    self.assertEqual(left_hints['node'], Optional[Node[T]])
    right_hints = get_type_hints(t.add_right, globals(), locals())
    self.assertEqual(right_hints['node'], Optional[Node[T]])
