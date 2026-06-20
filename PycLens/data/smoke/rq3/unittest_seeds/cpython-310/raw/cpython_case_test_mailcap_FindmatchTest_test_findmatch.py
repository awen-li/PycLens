# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: FindmatchTest_test_findmatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = MAILCAPDICT
    fname = 'foo.txt'
    plist = ['access-type=default', 'name=john', 'site=python.org', 'directory=/tmp', 'mode=foo', 'server=bar']
    audio_basic_entry = {'edit': 'audiocompose %s', 'compose': 'audiocompose %s', 'description': '"An audio fragment"', 'view': 'showaudio %s', 'lineno': 6}
    audio_entry = {'view': '/usr/local/bin/showaudio %t', 'lineno': 7}
    video_entry = {'view': 'animate %s', 'lineno': 12}
    message_entry = {'composetyped': 'extcompose %s', 'description': '"A reference to data stored in an external location"', 'needsterminal': '', 'view': 'showexternal %s %{access-type} %{name} %{site}     %{directory} %{mode} %{server}', 'lineno': 10}
    cases = [([{}, 'video/mpeg'], {}, (None, None)), ([c, 'foo/bar'], {}, (None, None)), ([c, 'video/mpeg'], {}, ('animate /dev/null', video_entry)), ([c, 'audio/basic', 'edit'], {}, ('audiocompose /dev/null', audio_basic_entry)), ([c, 'audio/basic', 'compose'], {}, ('audiocompose /dev/null', audio_basic_entry)), ([c, 'audio/basic', 'description'], {}, ('"An audio fragment"', audio_basic_entry)), ([c, 'audio/basic', 'foobar'], {}, (None, None)), ([c, 'video/*'], {'filename': fname}, ('animate %s' % fname, video_entry)), ([c, 'audio/basic', 'compose'], {'filename': fname}, ('audiocompose %s' % fname, audio_basic_entry)), ([c, 'audio/basic'], {'key': 'description', 'filename': fname}, ('"An audio fragment"', audio_basic_entry)), ([c, 'audio/*'], {'filename': fname}, (None, None)), ([c, 'audio/wav'], {'filename': fname}, ('/usr/local/bin/showaudio audio/wav', audio_entry)), ([c, 'message/external-body'], {'plist': plist}, ('showexternal /dev/null default john python.org     /tmp foo bar', message_entry))]
    self._run_cases(cases)
