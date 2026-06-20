# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_head_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO()
    (resp, info) = self.server.head(file=f)
    self.assertEqual(resp, '221 3000237 <45223423@example.com>')
    (art_num, message_id, lines) = info
    self.assertEqual(art_num, 3000237)
    self.assertEqual(message_id, '<45223423@example.com>')
    self.assertEqual(lines, [])
    data = f.getvalue()
    self.assertTrue(data.startswith(b'From: "Demo User" <nobody@example.net>\r\nSubject: I am just a test article\r\n'), ascii(data))
    self.assertFalse(data.endswith(b'This is just a test article.\r\n.Here is a dot-starting line.\r\n\r\n-- Signed by Andr\xc3\xa9.\r\n'), ascii(data))
