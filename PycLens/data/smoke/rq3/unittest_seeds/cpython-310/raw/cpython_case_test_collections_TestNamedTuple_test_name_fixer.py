# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_name_fixer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (spec, renamed) in [[('efg', 'g%hi'), ('efg', '_1')], [('abc', 'class'), ('abc', '_1')], [('8efg', '9ghi'), ('_0', '_1')], [('abc', '_efg'), ('abc', '_1')], [('abc', 'efg', 'efg', 'ghi'), ('abc', 'efg', '_2', 'ghi')], [('abc', '', 'x'), ('abc', '_1', 'x')]]:
        self.assertEqual(namedtuple('NT', spec, rename=True)._fields, renamed)
