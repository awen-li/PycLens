# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: PublicAPITests_test_module_all_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(nntplib, '__all__'))
    target_api = ['NNTP', 'NNTPError', 'NNTPReplyError', 'NNTPTemporaryError', 'NNTPPermanentError', 'NNTPProtocolError', 'NNTPDataError', 'decode_header']
    if ssl is not None:
        target_api.append('NNTP_SSL')
    self.assertEqual(set(nntplib.__all__), set(target_api))
