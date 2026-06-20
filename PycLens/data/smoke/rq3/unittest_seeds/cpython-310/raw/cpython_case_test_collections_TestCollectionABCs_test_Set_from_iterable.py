# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Set_from_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SetUsingInstanceFromIterable(MutableSet):

        def __init__(self, values, created_by):
            if not created_by:
                raise ValueError(f'created_by must be specified')
            self.created_by = created_by
            self._values = set(values)

        def _from_iterable(self, values):
            return type(self)(values, 'from_iterable')

        def __contains__(self, value):
            return value in self._values

        def __iter__(self):
            yield from self._values

        def __len__(self):
            return len(self._values)

        def add(self, value):
            self._values.add(value)

        def discard(self, value):
            self._values.discard(value)
    impl = SetUsingInstanceFromIterable([1, 2, 3], 'test')
    actual = impl - {1}
    self.assertIsInstance(actual, SetUsingInstanceFromIterable)
    self.assertEqual('from_iterable', actual.created_by)
    self.assertEqual({2, 3}, actual)
    actual = impl | {4}
    self.assertIsInstance(actual, SetUsingInstanceFromIterable)
    self.assertEqual('from_iterable', actual.created_by)
    self.assertEqual({1, 2, 3, 4}, actual)
    actual = impl & {2}
    self.assertIsInstance(actual, SetUsingInstanceFromIterable)
    self.assertEqual('from_iterable', actual.created_by)
    self.assertEqual({2}, actual)
    actual = impl ^ {3, 4}
    self.assertIsInstance(actual, SetUsingInstanceFromIterable)
    self.assertEqual('from_iterable', actual.created_by)
    self.assertEqual({1, 2, 4}, actual)
    impl ^= [3, 4]
    self.assertIsInstance(impl, SetUsingInstanceFromIterable)
    self.assertEqual('test', impl.created_by)
    self.assertEqual({1, 2, 4}, impl)
