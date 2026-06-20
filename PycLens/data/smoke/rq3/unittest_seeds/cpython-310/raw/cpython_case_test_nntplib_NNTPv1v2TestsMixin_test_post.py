# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_post

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_post_ihave(self.server.post, '240 Article received OK')
    self.handler.allow_posting = False
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.post(self.sample_post)
    self.assertEqual(cm.exception.response, '440 Posting not permitted')
