Welcome to logstash Ansible Role’s documentation!
=================================================

Role Name
---------

Ansible role to install and configure logstash over containers

### Requirements

Docker engine up and running.

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: logstash }

    #logstash_docker_image: docker.elastic.co/logstash/logstash
    logstash_docker_image: melodous/logstash
    logstash_version: 5.4.1
    logstash_monitoring: true
    logstash_check_logstashstatus: true
    logstash_group: logstash
    logstash_group_id: 1000
    logstash_user: logstash
    logstash_user_id: 1000
    logstash_output_es_hosts: localhost
    logstash_tcp_input_port: 4000
    conf_dir: /etc/logstash
    redis_ansible_group: indexers
    logstash_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_container_type: logstash

Changelog
---------

**logstash**

This project adheres to Semantic Versioning and human-readable
changelog.

### logstash master - unreleased

#### Added

-   First addition

#### Changed

-   First change

### logstash v0.0.1 - 2017/07/13

#### Added

-   Initial version

Copyright
---------

logstash

Copyright (C) 2017/07/12 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
