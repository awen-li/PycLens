# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_last

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, art_num, message_id) = self.server.last()
    self.assertEqual(resp, '223 3000234 <45223423@example.com> retrieved')
    self.assertEqual(art_num, 3000234)
    self.assertEqual(message_id, '<45223423@example.com>')
