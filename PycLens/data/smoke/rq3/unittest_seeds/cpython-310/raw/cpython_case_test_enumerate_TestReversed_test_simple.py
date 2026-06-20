# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __getitem__(self, i):
            if i < 5:
                return str(i)
            raise StopIteration

        def __len__(self):
            return 5
    for data in ('abc', range(5), tuple(enumerate('abc')), A(), range(1, 17, 5), dict.fromkeys('abcde')):
        self.assertEqual(list(data)[::-1], list(reversed(data)))
    self.assertRaises(TypeError, reversed, [], a=1)
