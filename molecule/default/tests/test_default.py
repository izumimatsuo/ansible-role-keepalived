import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_keepalived_is_installed(host):
    package = host.package("keepalived")
    assert package.is_installed
    assert package.version.startswith("1.3")
