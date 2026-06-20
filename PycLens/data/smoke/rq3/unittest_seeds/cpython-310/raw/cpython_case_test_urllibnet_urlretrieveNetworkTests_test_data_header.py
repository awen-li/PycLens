# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlretrieveNetworkTests_test_data_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlretrieve(self.logo) as (file_location, fileheaders):
        datevalue = fileheaders.get('Date')
        dateformat = '%a, %d %b %Y %H:%M:%S GMT'
        try:
            time.strptime(datevalue, dateformat)
        except ValueError:
            self.fail('Date value not in %r format' % dateformat)
