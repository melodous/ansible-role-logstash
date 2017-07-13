.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

Logstash packaging
------------------

.. envvar:: logstash_docker_imagen

   Logstash docker image

::

  logstash_docker_image: melodous/logstash




.. envvar:: logstash_version

   Logstash docker image version (TAG)

::

  logstash_version: 5.4.1




.. envvar:: logstash_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default logstash.

::

  logstash_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_container_type: logstash




Logstash configuration
----------------------

.. envvar:: logstash_group

   Logstash group name

::

  logstash_group: logstash




.. envvar:: logstash_group_id

   Logstash group id

::

  logstash_group_id: 1000




.. envvar:: logstash_user

   Logstash user name

::

  logstash_user: logstash




.. envvar:: logstash_user_id

   Logstash user id

::

  logstash_user_id: 1000




.. envvar:: logstash_output_es_hosts

   ElasticSerach host for output
   usually a list with all elastic search data nodes

::

  logstash_output_es_hosts: localhost




.. envvar:: logstash_tcp_input_port

   TCP port, for example to usage as input for fluentd

::

  logstash_tcp_input_port: 4000




.. envvar:: conf_dir

   Directory with logstash configuration and
   pipelines files

::

  conf_dir: /etc/logstash




.. envvar:: redis_ansible_group

   Ansible group that will be used as redis input

::

  redis_ansible_group: indexers




.. envvar:: logstash_heap_size

   Logstash java heap size, example 256m

::

  logstash_heap_size: 128m





Logstash monitoring management
------------------------------

.. envvar:: logstash_monitoring

   Enable or disable logstash monitoring
   ::

     logstash_monitoring: true




