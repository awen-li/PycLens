# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_system_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/')
    response = self.client.getresponse().read()
    self.assertIn(b'<dl><dt><a name="-system.methodHelp"><strong>system.methodHelp</strong></a>(method_name)</dt><dd><tt><a href="#-system.methodHelp">system.methodHelp</a>(\'add\')&nbsp;=&gt;&nbsp;"Adds&nbsp;two&nbsp;integers&nbsp;together"<br>\n&nbsp;<br>\nReturns&nbsp;a&nbsp;string&nbsp;containing&nbsp;documentation&nbsp;for&nbsp;the&nbsp;specified&nbsp;method.</tt></dd></dl>\n<dl><dt><a name="-system.methodSignature"><strong>system.methodSignature</strong></a>(method_name)</dt><dd><tt><a href="#-system.methodSignature">system.methodSignature</a>(\'add\')&nbsp;=&gt;&nbsp;[double,&nbsp;int,&nbsp;int]<br>\n&nbsp;<br>\nReturns&nbsp;a&nbsp;list&nbsp;describing&nbsp;the&nbsp;signature&nbsp;of&nbsp;the&nbsp;method.&nbsp;In&nbsp;the<br>\nabove&nbsp;example,&nbsp;the&nbsp;add&nbsp;method&nbsp;takes&nbsp;two&nbsp;integers&nbsp;as&nbsp;arguments<br>\nand&nbsp;returns&nbsp;a&nbsp;double&nbsp;result.<br>\n&nbsp;<br>\nThis&nbsp;server&nbsp;does&nbsp;NOT&nbsp;support&nbsp;system.methodSignature.</tt></dd></dl>', response)
