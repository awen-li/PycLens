# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_article_head_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, count, first, last, name) = self.server.group(self.GROUP_NAME)
    for art_num in (last, first, last - 1):
        try:
            (resp, head) = self.server.head(art_num)
        except nntplib.NNTPTemporaryError as e:
            if not e.response.startswith('423 '):
                raise
            continue
        break
    else:
        self.skipTest('could not find a suitable article number')
    self.assertTrue(resp.startswith('221 '), resp)
    self.check_article_resp(resp, head, art_num)
    (resp, body) = self.server.body(art_num)
    self.assertTrue(resp.startswith('222 '), resp)
    self.check_article_resp(resp, body, art_num)
    (resp, article) = self.server.article(art_num)
    self.assertTrue(resp.startswith('220 '), resp)
    self.check_article_resp(resp, article, art_num)
    denylist = lambda line: line.startswith(b'X-Antivirus')
    filtered_head_lines = [line for line in head.lines if not denylist(line)]
    filtered_lines = [line for line in article.lines if not denylist(line)]
    self.assertEqual(filtered_lines, filtered_head_lines + [b''] + body.lines)
