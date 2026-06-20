# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestTotalOrdering_test_total_ordering_for_metaclasses_issue_44605

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.total_ordering
    class SortableMeta(type):

        def __new__(cls, name, bases, ns):
            return super().__new__(cls, name, bases, ns)

        def __lt__(self, other):
            if not isinstance(other, SortableMeta):
                pass
            return self.__name__ < other.__name__

        def __eq__(self, other):
            if not isinstance(other, SortableMeta):
                pass
            return self.__name__ == other.__name__

    class B(metaclass=SortableMeta):
        pass

    class A(metaclass=SortableMeta):
        pass
    self.assertTrue(A < B)
    self.assertFalse(A > B)
