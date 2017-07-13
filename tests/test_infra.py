def test_logstash_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that logstash service is running and enabled
    logstash_service = Service("logstash")
    assert logstash_service.is_running
    assert logstash_service.is_enabled


def test_logstash_start_stop(Command, Service):
    Command.run_expect([0], "systemctl stop logstash")
    logstash_service = Service("logstash")
    assert not logstash_service.is_running
    Command.run_expect([0], "systemctl start logstash")
    assert logstash_service.is_running
    Command.run_expect([0], "systemctl restart logstash")
    assert logstash_service.is_running


def test_socket(Socket):
    # Check logstash port is up and running
    assert Socket("tcp://0.0.0.0:4000").is_listening
    assert Socket("tcp://0.0.0.0:9600").is_listening


def test_monitoring(Command, Ansible):
    from zabbix_api import ZabbixAPI
    zbx_if = Ansible("setup")['ansible_facts']['ansible_enp0s8']
    zbx_ip = zbx_if['ipv4']['address']
    zbx = ZabbixAPI("http://%s" % zbx_ip, timeout=10)
    zbx.login("Admin", "zabbix")
    zbx_host_list = get_host_by_host_name(zbx, "logstash")
    assert len(zbx_host_list) == 1
    zbx_host = zbx_host_list[0]['hostid']
    item = zbx.item.get(
        {
            "output": ["lastvalue"],
            "hostids": zbx_host,
            "search": {
                "key_": "logstash.heartbeat"
            },
            "startSearch": "true"
        }
    )
    assert item[0]['lastvalue'] > '1'
#    Command.run_expect([0], "systemctl stop logstash")
#    check_item(zbx, zbx_host, "logstash.heartbeat", '0', 120)
#    Command.run_expect([0], "systemctl start logstash")
#    check_item(zbx, zbx_host, "logstash.heartbeat", '1', 120)


def check_item(zbx, host, key, value, timeout):
    import datetime
    import time
    init = datetime.datetime.now()
    while True:
        item = zbx.item.get(
                {
                    "output": ["lastvalue"],
                    "hostids": host,
                    "search": {
                        "key_": key
                    },
                    "startSearch": "true"
                }
            )
        if item[0]['lastvalue'] == value:
            break
        diff = (datetime.datetime.now() - init).total_seconds()
        assert int(diff) < timeout
        time.sleep(5)


def get_host_by_host_name(zbx, host_name):
    host_list = zbx.host.get(
            {
                'output': 'extend', 'filter': {'host': [host_name]}
            }
        )
    return host_list
