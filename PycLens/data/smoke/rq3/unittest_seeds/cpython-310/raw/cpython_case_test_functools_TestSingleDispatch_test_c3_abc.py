# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_c3_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = collections.abc
    mro = functools._c3_mro

    class A(object):
        pass

    class B(A):

        def __len__(self):
            return 0

    @c.Container.register
    class C(object):
        pass

    class D(object):
        pass

    class X(D, C, B):

        def __call__(self):
            pass
    expected = [X, c.Callable, D, C, c.Container, B, c.Sized, A, object]
    for abcs in permutations([c.Sized, c.Callable, c.Container]):
        self.assertEqual(mro(X, abcs=abcs), expected)
    many_abcs = [c.Mapping, c.Sized, c.Callable, c.Container, c.Iterable]
    self.assertEqual(mro(X, abcs=many_abcs), expected)
