import pytest

def test_logstash_server_running_and_enabled(Command,Service):
  # Check that docker service is running and enabled
  docker_service = Service("docker")
  assert docker_service.is_running
  assert docker_service.is_enabled
  # Check that logstash service is running and enabled
  logstash_service = Service("logstash")
  assert logstash_service.is_running
  assert logstash_service.is_enabled

  # Check that logstash-cli ping
  logstash_output = Command.check_output("docker exec logstash logstash-cli ping")
  assert logstash_output == "PONG"

def test_logstash_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop logstash")
  logstash_service = Service("logstash")
  assert not logstash_service.is_running
  Command.run_expect([0],"systemctl start logstash")
  assert logstash_service.is_running
  Command.run_expect([0],"systemctl restart logstash")
  assert logstash_service.is_running
  logstash_output = Command.check_output("docker exec logstash logstash-cli ping")
  assert logstash_output == "PONG"
