# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_article

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, info) = self.server.article()
    self.assertEqual(resp, '220 3000237 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 3000237)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_data(lines)
    (resp, info) = self.server.article(3000234)
    self.assertEqual(resp, '220 3000234 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 3000234)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_data(lines)
    (resp, info) = self.server.article('<45223423@example.com>')
    self.assertEqual(resp, '220 0 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 0)
    self.assertEqual(message_id, '<45223423@example.com>')
    self._check_article_data(lines)
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.article('<non-existent@example.com>')
    self.assertEqual(cm.exception.response, '430 No Such Article Found')
