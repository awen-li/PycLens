# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_issue28598_strsubclass_rhs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SubclassedStr(str):

        def __rmod__(self, other):
            return 'Success, self.__rmod__({!r}) was called'.format(other)
    self.assertEqual('lhs %% %r' % SubclassedStr('rhs'), "Success, self.__rmod__('lhs %% %r') was called")
