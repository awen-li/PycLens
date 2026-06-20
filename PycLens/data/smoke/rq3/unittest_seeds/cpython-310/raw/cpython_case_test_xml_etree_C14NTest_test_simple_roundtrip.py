# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: C14NTest_test_simple_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(c14n_roundtrip('<doc/>'), '<doc></doc>')
    self.assertEqual(c14n_roundtrip("<doc xmlns='uri'/>"), '<doc xmlns="uri"></doc>')
    self.assertEqual(c14n_roundtrip("<prefix:doc xmlns:prefix='uri'/>"), '<prefix:doc xmlns:prefix="uri"></prefix:doc>')
    self.assertEqual(c14n_roundtrip("<doc xmlns:prefix='uri'><prefix:bar/></doc>"), '<doc><prefix:bar xmlns:prefix="uri"></prefix:bar></doc>')
    self.assertEqual(c14n_roundtrip("<elem xmlns:wsu='http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd' xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' />"), '<elem></elem>')
    self.assertEqual(c14n_roundtrip('<doc>Hello, world!<!-- Comment 1 --></doc>'), '<doc>Hello, world!</doc>')
    self.assertEqual(c14n_roundtrip('<value>&#x32;</value>'), '<value>2</value>')
    self.assertEqual(c14n_roundtrip('<compute><![CDATA[value>"0" && value<"10" ?"valid":"error"]]></compute>'), '<compute>value&gt;"0" &amp;&amp; value&lt;"10" ?"valid":"error"</compute>')
    self.assertEqual(c14n_roundtrip('<compute expr=\'value>"0" &amp;&amp; value&lt;"10" ?"valid":"error"\'>valid</compute>'), '<compute expr="value>&quot;0&quot; &amp;&amp; value&lt;&quot;10&quot; ?&quot;valid&quot;:&quot;error&quot;">valid</compute>')
    self.assertEqual(c14n_roundtrip("<norm attr=' &apos;   &#x20;&#13;&#xa;&#9;   &apos; '/>"), '<norm attr=" \'    &#xD;&#xA;&#x9;   \' "></norm>')
    self.assertEqual(c14n_roundtrip("<normNames attr='   A   &#x20;&#13;&#xa;&#9;   B   '/>"), '<normNames attr="   A    &#xD;&#xA;&#x9;   B   "></normNames>')
    self.assertEqual(c14n_roundtrip("<normId id=' &apos;   &#x20;&#13;&#xa;&#9;   &apos; '/>"), '<normId id=" \'    &#xD;&#xA;&#x9;   \' "></normId>')
    xml = '<X xmlns="http://nps/a"><Y targets="abc,xyz"></Y></X>'
    self.assertEqual(c14n_roundtrip(xml), xml)
    xml = '<X xmlns="http://nps/a"><Y xmlns="http://nsp/b" targets="abc,xyz"></Y></X>'
    self.assertEqual(c14n_roundtrip(xml), xml)
    xml = '<X xmlns="http://nps/a"><Y xmlns:b="http://nsp/b" b:targets="abc,xyz"></Y></X>'
    self.assertEqual(c14n_roundtrip(xml), xml)
