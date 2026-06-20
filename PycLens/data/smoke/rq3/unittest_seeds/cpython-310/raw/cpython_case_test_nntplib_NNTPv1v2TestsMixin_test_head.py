# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, info) = self.server.head()
    self.assertEqual(resp, '221 3000237 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 3000237)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_head(lines)
    (resp, info) = self.server.head(3000234)
    self.assertEqual(resp, '221 3000234 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 3000234)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_head(lines)
    (resp, info) = self.server.head('<45223423@example.com>')
    self.assertEqual(resp, '221 0 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 0)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_head(lines)
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.head('<non-existent@example.com>')
    self.assertEqual(cm.exception.response, '430 No Such Article Found')
