Role Name
=========

Ansible role to install and configure logstash over containers

Requirements
------------

Docker engine up and running.

Dependencies
------------

N/A

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: logstash }
