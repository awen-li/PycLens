# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_rich_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestRichSetCompare:

        def __gt__(self, some_set):
            self.gt_called = True
            return False

        def __lt__(self, some_set):
            self.lt_called = True
            return False

        def __ge__(self, some_set):
            self.ge_called = True
            return False

        def __le__(self, some_set):
            self.le_called = True
            return False
    myset = {1, 2, 3}
    myobj = TestRichSetCompare()
    myset < myobj
    self.assertTrue(myobj.gt_called)
    myobj = TestRichSetCompare()
    myset > myobj
    self.assertTrue(myobj.lt_called)
    myobj = TestRichSetCompare()
    myset <= myobj
    self.assertTrue(myobj.ge_called)
    myobj = TestRichSetCompare()
    myset >= myobj
    self.assertTrue(myobj.le_called)
