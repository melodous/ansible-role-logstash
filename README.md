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

pip ansible role default variables
----------------------------------

#### Sections

-   Logstash packaging
-   Logstash configuration
-   Logstash monitoring management

### Logstash packaging

`logstash_docker_imagen`

> Logstash docker image

    logstash_docker_image: melodous/logstash

`logstash_version`

> Logstash docker image version (TAG)

    logstash_version: 5.4.1

`logstash_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default logstash.

    logstash_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_container_type: logstash

### Logstash configuration

`logstash_group`

> Logstash group name

    logstash_group: logstash

`logstash_group_id`

> Logstash group id

    logstash_group_id: 1000

`logstash_user`

> Logstash user name

    logstash_user: logstash

`logstash_user_id`

> Logstash user id

    logstash_user_id: 1000

`logstash_output_es_hosts`

> ElasticSerach host for output usually a list with all elastic search
> data nodes

    logstash_output_es_hosts: localhost

`logstash_tcp_input_port`

> TCP port, for example to usage as input for fluentd

    logstash_tcp_input_port: 4000

`conf_dir`

> Directory with logstash configuration and pipelines files

    conf_dir: /etc/logstash

`redis_ansible_group`

> Ansible group that will be used as redis input

    redis_ansible_group: indexers

`zabbix_server`

> Zabbix server for output

    zabbix_server: localhost

`logstash_heap_size`

> Logstash java heap size, example 256m

    logstash_heap_size: 128m

### Logstash monitoring management

`logstash_monitoring`

> Enable or disable logstash monitoring
>
>     logstash_monitoring: true

Changelog
---------

**logstash**

This project adheres to Semantic Versioning and human-readable
changelog.

### logstash master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### logstash v0.0.2 - 2017/08/08

##### Changed

-   Updated grok filters for finanzas openshift project

### logstash v0.0.3 - 2017/07/21

##### Changed

-   Added filters for openshift projects

### logstash v0.0.2 - 2017/07/17

##### Changed

-   Fixed zabbix\_host on filters

### logstash v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

logstash

Copyright (C) 2017/07/12 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
