# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_serialization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pickled_posonly = pickle.dumps(global_pos_only_f)
    pickled_optional = pickle.dumps(global_pos_only_and_normal)
    pickled_defaults = pickle.dumps(global_pos_only_defaults)
    unpickled_posonly = pickle.loads(pickled_posonly)
    unpickled_optional = pickle.loads(pickled_optional)
    unpickled_defaults = pickle.loads(pickled_defaults)
    self.assertEqual(unpickled_posonly(1, 2), (1, 2))
    expected = "global_pos_only_f\\(\\) got some positional-only arguments passed as keyword arguments: 'a, b'"
    with self.assertRaisesRegex(TypeError, expected):
        unpickled_posonly(a=1, b=2)
    self.assertEqual(unpickled_optional(1, 2), (1, 2))
    expected = "global_pos_only_and_normal\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"
    with self.assertRaisesRegex(TypeError, expected):
        unpickled_optional(a=1, b=2)
    self.assertEqual(unpickled_defaults(), (1, 2))
    expected = "global_pos_only_defaults\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"
    with self.assertRaisesRegex(TypeError, expected):
        unpickled_defaults(a=1, b=2)
