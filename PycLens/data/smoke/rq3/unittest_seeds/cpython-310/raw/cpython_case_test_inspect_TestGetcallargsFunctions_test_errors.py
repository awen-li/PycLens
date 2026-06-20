# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetcallargsFunctions_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f0 = self.makeCallable('')
    f1 = self.makeCallable('a, b')
    f2 = self.makeCallable('a, b=1')
    self.assertEqualException(f0, '1')
    self.assertEqualException(f0, 'x=1')
    self.assertEqualException(f0, '1,x=1')
    self.assertEqualException(f1, '')
    self.assertEqualException(f1, '1')
    self.assertEqualException(f1, 'a=2')
    self.assertEqualException(f1, 'b=3')
    self.assertEqualException(f2, '')
    self.assertEqualException(f2, 'b=3')
    for f in (f1, f2):
        self.assertEqualException(f, '2, 3, 4')
        self.assertEqualException(f, '1, 2, 3, a=1')
        self.assertEqualException(f, '2, 3, 4, c=5')
        self.assertEqualException(f, 'c=2')
        self.assertEqualException(f, '2, c=3')
        self.assertEqualException(f, '2, 3, c=4')
        self.assertEqualException(f, '2, c=4, b=3')
        self.assertEqualException(f, '**{u"πι": 4}')
        self.assertEqualException(f, '1, a=2')
        self.assertEqualException(f, '1, **{"a":2}')
        self.assertEqualException(f, '1, 2, b=3')
    f3 = self.makeCallable('**c')
    self.assertEqualException(f3, '1, 2')
    self.assertEqualException(f3, '1, 2, a=1, b=2')
    f4 = self.makeCallable('*, a, b=0')
    self.assertEqualException(f3, '1, 2')
    self.assertEqualException(f3, '1, 2, a=1, b=2')

    def f5(*, a):
        pass
    with self.assertRaisesRegex(TypeError, 'missing 1 required keyword-only'):
        inspect.getcallargs(f5)

    def f6(a, b, c):
        pass
    with self.assertRaisesRegex(TypeError, "'a', 'b' and 'c'"):
        inspect.getcallargs(f6)
    with self.assertRaisesRegex(ValueError, 'variadic keyword parameters cannot have default values'):
        inspect.Parameter('foo', kind=inspect.Parameter.VAR_KEYWORD, default=42)
    with self.assertRaisesRegex(ValueError, 'value 5 is not a valid Parameter.kind'):
        inspect.Parameter('bar', kind=5, default=42)
    with self.assertRaisesRegex(TypeError, 'name must be a str, not a int'):
        inspect.Parameter(123, kind=4)
