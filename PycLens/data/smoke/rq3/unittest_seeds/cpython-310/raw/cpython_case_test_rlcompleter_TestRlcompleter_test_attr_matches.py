# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_attr_matches

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.stdcompleter.attr_matches('str.s'), ['str.{}('.format(x) for x in dir(str) if x.startswith('s')])
    self.assertEqual(self.stdcompleter.attr_matches('tuple.foospamegg'), [])
    expected = sorted({'None.%s%s' % (x, '(' if x != '__doc__' else '') for x in dir(None)})
    self.assertEqual(self.stdcompleter.attr_matches('None.'), expected)
    self.assertEqual(self.stdcompleter.attr_matches('None._'), expected)
    self.assertEqual(self.stdcompleter.attr_matches('None.__'), expected)
    self.assertEqual(self.completer.attr_matches('CompleteMe.sp'), ['CompleteMe.spam'])
    self.assertEqual(self.completer.attr_matches('Completeme.egg'), [])
    self.assertEqual(self.completer.attr_matches('CompleteMe.'), ['CompleteMe.mro()', 'CompleteMe.spam'])
    self.assertEqual(self.completer.attr_matches('CompleteMe._'), ['CompleteMe._ham'])
    matches = self.completer.attr_matches('CompleteMe.__')
    for x in matches:
        self.assertTrue(x.startswith('CompleteMe.__'), x)
    self.assertIn('CompleteMe.__name__', matches)
    self.assertIn('CompleteMe.__new__(', matches)
    with patch.object(CompleteMe, 'me', CompleteMe, create=True):
        self.assertEqual(self.completer.attr_matches('CompleteMe.me.me.sp'), ['CompleteMe.me.me.spam'])
        self.assertEqual(self.completer.attr_matches('egg.s'), ['egg.{}('.format(x) for x in dir(str) if x.startswith('s')])
