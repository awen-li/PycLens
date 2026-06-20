# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_namedtuple_keyword_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    LocalEmployee = NamedTuple('LocalEmployee', name=str, age=int)
    nick = LocalEmployee('Nick', 25)
    self.assertIsInstance(nick, tuple)
    self.assertEqual(nick.name, 'Nick')
    self.assertEqual(LocalEmployee.__name__, 'LocalEmployee')
    self.assertEqual(LocalEmployee._fields, ('name', 'age'))
    self.assertEqual(LocalEmployee.__annotations__, dict(name=str, age=int))
    with self.assertRaises(TypeError):
        NamedTuple('Name', [('x', int)], y=str)
    with self.assertRaises(TypeError):
        NamedTuple('Name', x=1, y='a')
