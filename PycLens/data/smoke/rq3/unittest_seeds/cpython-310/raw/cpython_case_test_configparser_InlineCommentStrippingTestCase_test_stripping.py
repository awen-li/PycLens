# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: InlineCommentStrippingTestCase_test_stripping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg = configparser.ConfigParser(inline_comment_prefixes=(';', '#', '//'))
    cfg.read_string('\n        [section]\n        k1 = v1;still v1\n        k2 = v2 ;a comment\n        k3 = v3 ; also a comment\n        k4 = v4;still v4 ;a comment\n        k5 = v5;still v5 ; also a comment\n        k6 = v6;still v6; and still v6 ;a comment\n        k7 = v7;still v7; and still v7 ; also a comment\n\n        [multiprefix]\n        k1 = v1;still v1 #a comment ; yeah, pretty much\n        k2 = v2 // this already is a comment ; continued\n        k3 = v3;#//still v3# and still v3 ; a comment\n        ')
    s = cfg['section']
    self.assertEqual(s['k1'], 'v1;still v1')
    self.assertEqual(s['k2'], 'v2')
    self.assertEqual(s['k3'], 'v3')
    self.assertEqual(s['k4'], 'v4;still v4')
    self.assertEqual(s['k5'], 'v5;still v5')
    self.assertEqual(s['k6'], 'v6;still v6; and still v6')
    self.assertEqual(s['k7'], 'v7;still v7; and still v7')
    s = cfg['multiprefix']
    self.assertEqual(s['k1'], 'v1;still v1')
    self.assertEqual(s['k2'], 'v2')
    self.assertEqual(s['k3'], 'v3;#//still v3# and still v3')
