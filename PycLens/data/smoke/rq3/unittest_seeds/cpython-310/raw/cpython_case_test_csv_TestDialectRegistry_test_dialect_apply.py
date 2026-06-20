# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_dialect_apply

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class testA(csv.excel):
        delimiter = '\t'

    class testB(csv.excel):
        delimiter = ':'

    class testC(csv.excel):
        delimiter = '|'

    class testUni(csv.excel):
        delimiter = 'Λ'

    class unspecified:
        pass
    csv.register_dialect('testC', testC)
    try:
        self.compare_dialect_123('1,2,3\r\n')
        self.compare_dialect_123('1,2,3\r\n', dialect=None)
        self.compare_dialect_123('1,2,3\r\n', dialect=unspecified)
        self.compare_dialect_123('1\t2\t3\r\n', testA)
        self.compare_dialect_123('1:2:3\r\n', dialect=testB())
        self.compare_dialect_123('1|2|3\r\n', dialect='testC')
        self.compare_dialect_123('1;2;3\r\n', dialect=testA, delimiter=';')
        self.compare_dialect_123('1Λ2Λ3\r\n', dialect=testUni)
    finally:
        csv.unregister_dialect('testC')
