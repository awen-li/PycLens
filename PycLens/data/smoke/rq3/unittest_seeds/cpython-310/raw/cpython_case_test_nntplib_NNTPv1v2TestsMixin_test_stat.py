# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_stat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, art_num, message_id) = self.server.stat(3000234)
    self.assertEqual(resp, '223 3000234 <45223423@example.com>')
    self.assertEqual(art_num, 3000234)
    self.assertEqual(message_id, '<45223423@example.com>')
    (resp, art_num, message_id) = self.server.stat('<45223423@example.com>')
    self.assertEqual(resp, '223 0 <45223423@example.com>')
    self.assertEqual(art_num, 0)
    self.assertEqual(message_id, '<45223423@example.com>')
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.stat('<non.existent.id>')
    self.assertEqual(cm.exception.response, '430 No Such Article Found')
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.stat()
    self.assertEqual(cm.exception.response, '412 No newsgroup selected')
