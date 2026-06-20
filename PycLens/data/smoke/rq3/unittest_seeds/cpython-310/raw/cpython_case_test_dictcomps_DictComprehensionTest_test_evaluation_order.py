# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictcomps.py
# case: DictComprehensionTest_test_evaluation_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = {'H': 'W', 'e': 'o', 'l': 'l', 'o': 'd'}
    expected_calls = [('key', 'H'), ('value', 'W'), ('key', 'e'), ('value', 'o'), ('key', 'l'), ('value', 'r'), ('key', 'l'), ('value', 'l'), ('key', 'o'), ('value', 'd')]
    actual_calls = []

    def add_call(pos, value):
        actual_calls.append((pos, value))
        return value
    actual = {add_call('key', k): add_call('value', v) for (k, v) in zip('Hello', 'World')}
    self.assertEqual(actual, expected)
    self.assertEqual(actual_calls, expected_calls)
