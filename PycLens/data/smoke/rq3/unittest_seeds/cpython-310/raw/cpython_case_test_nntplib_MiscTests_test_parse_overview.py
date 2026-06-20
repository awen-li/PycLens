# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MiscTests_test_parse_overview

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = nntplib._DEFAULT_OVERVIEW_FMT + ['xref']
    lines = ['3000234\tI am just a test article\t"Demo User" <nobody@example.com>\t6 Oct 1998 04:38:40 -0500\t<45223423@example.com>\t<45454@example.net>\t1234\t17\tXref: news.example.com misc.test:3000363']
    overview = nntplib._parse_overview(lines, fmt)
    ((art_num, fields),) = overview
    self.assertEqual(art_num, 3000234)
    self.assertEqual(fields, {'subject': 'I am just a test article', 'from': '"Demo User" <nobody@example.com>', 'date': '6 Oct 1998 04:38:40 -0500', 'message-id': '<45223423@example.com>', 'references': '<45454@example.net>', ':bytes': '1234', ':lines': '17', 'xref': 'news.example.com misc.test:3000363'})
    lines = ['3000234\tI am just a test article\t"Demo User" <nobody@example.com>\t6 Oct 1998 04:38:40 -0500\t<45223423@example.com>\t<45454@example.net>\t1234\t17\t\t']
    overview = nntplib._parse_overview(lines, fmt)
    ((art_num, fields),) = overview
    self.assertEqual(fields['xref'], None)
    lines = ['3000234\tI am just a test article\t"Demo User" <nobody@example.com>\t6 Oct 1998 04:38:40 -0500\t<45223423@example.com>\t \t1234\t17\tXref: \t']
    overview = nntplib._parse_overview(lines, fmt)
    ((art_num, fields),) = overview
    self.assertEqual(fields['references'], ' ')
    self.assertEqual(fields['xref'], '')
