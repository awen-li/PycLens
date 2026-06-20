# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: CGIHandlerTestCase_test_cgi_xmlrpc_response

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = "<?xml version='1.0'?>\n        <methodCall>\n            <methodName>test_method</methodName>\n            <params>\n                <param>\n                    <value><string>foo</string></value>\n                </param>\n                <param>\n                    <value><string>bar</string></value>\n                </param>\n            </params>\n        </methodCall>\n        "
    with os_helper.EnvironmentVarGuard() as env, captured_stdout(encoding=self.cgi.encoding) as data_out, support.captured_stdin() as data_in:
        data_in.write(data)
        data_in.seek(0)
        env['CONTENT_LENGTH'] = str(len(data))
        self.cgi.handle_request()
    data_out.seek(0)
    handle = data_out.read()
    self.assertRaises(xmlrpclib.Fault, xmlrpclib.loads, handle[44:])
    content = handle[handle.find('<?xml'):]
    self.assertEqual(int(re.search('Content-Length: (\\d+)', handle).group(1)), len(content))
