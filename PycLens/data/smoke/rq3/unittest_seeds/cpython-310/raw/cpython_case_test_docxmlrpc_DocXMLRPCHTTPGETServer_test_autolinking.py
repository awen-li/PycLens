# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_autolinking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/')
    response = self.client.getresponse().read()
    self.assertIn(b'<dl><dt><a name="-add"><strong>add</strong></a>(x, y)</dt><dd><tt>Add&nbsp;two&nbsp;instances&nbsp;together.&nbsp;This&nbsp;follows&nbsp;<a href="https://www.python.org/dev/peps/pep-0008/">PEP008</a>,&nbsp;but&nbsp;has&nbsp;nothing<br>\nto&nbsp;do&nbsp;with&nbsp;<a href="http://www.rfc-editor.org/rfc/rfc1952.txt">RFC1952</a>.&nbsp;Case&nbsp;should&nbsp;matter:&nbsp;pEp008&nbsp;and&nbsp;rFC1952.&nbsp;&nbsp;Things<br>\nthat&nbsp;start&nbsp;with&nbsp;http&nbsp;and&nbsp;ftp&nbsp;should&nbsp;be&nbsp;auto-linked,&nbsp;too:<br>\n<a href="http://google.com">http://google.com</a>.</tt></dd></dl>', response)
