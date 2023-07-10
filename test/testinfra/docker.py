import json
conf = open('conf/packer/vars/docker.json', 'r')
version = json.loads(conf.read())['version']

def test_version_via_default(host):
    cmd = host.run_expect([0], 'docker run cliffano/rtk --version')
    assert cmd.stdout == '2.3.0\n'

def test_help_via_default(host):
    cmd = host.run_expect([0], 'docker run cliffano/rtk --help')
    assert 'Usage: rtk [options] [command]' in cmd.stdout

def test_version_via_latest_tag(host):
    cmd = host.run_expect([0], 'docker run cliffano/rtk:latest --version')
    assert cmd.stdout == '2.3.0\n'

def test_help_via_latest_tag(host):
    cmd = host.run_expect([0], 'docker run cliffano/rtk:latest --help')
    assert 'Usage: rtk [options] [command]' in cmd.stdout

def test_version_via_version_tag(host):
    cmd = host.run_expect([0], f'docker run cliffano/rtk:{version} --version')
    assert cmd.stdout == '2.3.0\n'

def test_help_via_version_tag(host):
    cmd = host.run_expect([0], f'docker run cliffano/rtk:{version} --help')
    assert 'Usage: rtk [options] [command]' in cmd.stdout
