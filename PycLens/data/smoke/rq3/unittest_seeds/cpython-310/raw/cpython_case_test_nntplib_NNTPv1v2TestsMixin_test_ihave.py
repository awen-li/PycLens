# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_ihave

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_post_ihave(self.server.ihave, '235 Article transferred OK', '<i.am.an.article.you.will.want@example.com>')
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.ihave('<another.message.id>', self.sample_post)
    self.assertEqual(cm.exception.response, '435 Article not wanted')
