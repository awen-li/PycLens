# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MiscTests_test_parse_overview_fmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = ['Subject:', 'From:', 'Date:', 'Message-ID:', 'References:', ':bytes', ':lines']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines'])
    lines = ['Subject:', 'From:', 'Date:', 'Message-ID:', 'References:', 'Bytes:', 'Lines:']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines'])
    lines = ['subject:', 'FROM:', 'DaTe:', 'message-ID:', 'References:', 'BYTES:', 'Lines:']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines'])
    lines = ['Subject:', 'From:', 'Date:', 'Message-ID:', 'References:', ':bytes', ':lines', 'Xref:full', 'Distribution:full']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines', 'xref', 'distribution'])
    lines = ['Subject:', 'From:', 'Date:', 'Message-ID:', 'References:', 'Bytes:', 'Lines:', 'Xref:FULL', 'Distribution:FULL']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines', 'xref', 'distribution'])
    lines = ['Subject:', 'From:', 'Date:', 'Message-ID:', 'References:', 'Bytes:', 'Lines:', 'Xref:full']
    self.assertEqual(nntplib._parse_overview_fmt(lines), ['subject', 'from', 'date', 'message-id', 'references', ':bytes', ':lines', 'xref'])
