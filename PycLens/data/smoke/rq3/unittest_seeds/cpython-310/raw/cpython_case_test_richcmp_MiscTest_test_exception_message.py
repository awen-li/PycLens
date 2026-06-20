# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: MiscTest_test_exception_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Spam:
        pass
    tests = [(lambda : 42 < None, "'<' .* of 'int' and 'NoneType'"), (lambda : None < 42, "'<' .* of 'NoneType' and 'int'"), (lambda : 42 > None, "'>' .* of 'int' and 'NoneType'"), (lambda : 'foo' < None, "'<' .* of 'str' and 'NoneType'"), (lambda : 'foo' >= 666, "'>=' .* of 'str' and 'int'"), (lambda : 42 <= None, "'<=' .* of 'int' and 'NoneType'"), (lambda : 42 >= None, "'>=' .* of 'int' and 'NoneType'"), (lambda : 42 < [], "'<' .* of 'int' and 'list'"), (lambda : () > [], "'>' .* of 'tuple' and 'list'"), (lambda : None >= None, "'>=' .* of 'NoneType' and 'NoneType'"), (lambda : Spam() < 42, "'<' .* of 'Spam' and 'int'"), (lambda : 42 < Spam(), "'<' .* of 'int' and 'Spam'"), (lambda : Spam() <= Spam(), "'<=' .* of 'Spam' and 'Spam'")]
    for (i, test) in enumerate(tests):
        with self.subTest(test=i):
            with self.assertRaisesRegex(TypeError, test[1]):
                test[0]()
