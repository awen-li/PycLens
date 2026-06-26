# Source Generated with Decompyle++
# File: cpython-310-1933bbc9617a.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class TestRichSetCompare:
        __module__ = __name__
        __qualname__ = '__pybcsec_seed__.<locals>.TestRichSetCompare'
        
        def __gt__(self, some_set):
            self.gt_called = True
            return False

    # WARNING: Decompyle incomplete

    myset = {
        1,
        2,
        3}
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

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
