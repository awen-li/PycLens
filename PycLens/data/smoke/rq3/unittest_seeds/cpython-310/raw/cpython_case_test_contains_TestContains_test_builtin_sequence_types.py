# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contains.py
# case: TestContains_test_builtin_sequence_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = range(10)
    for i in a:
        self.assertIn(i, a)
    self.assertNotIn(16, a)
    self.assertNotIn(a, a)
    a = tuple(a)
    for i in a:
        self.assertIn(i, a)
    self.assertNotIn(16, a)
    self.assertNotIn(a, a)

    class Deviant1:
        """Behaves strangely when compared

            This class is designed to make sure that the contains code
            works when the list is modified during the check.
            """
        aList = list(range(15))

        def __eq__(self, other):
            if other == 12:
                self.aList.remove(12)
                self.aList.remove(13)
                self.aList.remove(14)
            return 0
    self.assertNotIn(Deviant1(), Deviant1.aList)
