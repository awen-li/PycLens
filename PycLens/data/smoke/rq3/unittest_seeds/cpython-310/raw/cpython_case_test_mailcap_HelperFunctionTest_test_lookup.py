# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: HelperFunctionTest_test_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [{'view': 'animate %s', 'lineno': 12}, {'view': 'mpeg_play %s', 'lineno': 13}]
    actual = mailcap.lookup(MAILCAPDICT, 'video/mpeg')
    self.assertListEqual(expected, actual)
    key = 'compose'
    expected = [{'edit': 'audiocompose %s', 'compose': 'audiocompose %s', 'description': '"An audio fragment"', 'view': 'showaudio %s', 'lineno': 6}]
    actual = mailcap.lookup(MAILCAPDICT, 'audio/basic', key)
    self.assertListEqual(expected, actual)
    expected = [{'view': 'mpeg_play %s'}, {'view': 'animate %s'}]
    actual = mailcap.lookup(MAILCAPDICT_DEPRECATED, 'video/mpeg')
    self.assertListEqual(expected, actual)
