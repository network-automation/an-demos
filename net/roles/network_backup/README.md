Role Name
=========

This role backs up the configuration of a network device if a backup does not exist and detects differences in the device's configuration with the previsous backup if it does exist.

The file is backed up to "{{ net_backup_root }}/{{ inventory_hostname }}"

The backup can be forced by setting net_backup_force "true"

Requirements
------------

Currently supports:
- ios
- nxos

Role Variables
--------------

    net_backup_root
    net_backup_force
    
Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: network
      connection: local
      gather_facts: no

      tasks:
        - include_role:
            name: net-backup
          vars:
            net_backup_root: /data/backups

The playook can be run to either backup or check for changes:

    ansible-playbook -i hosts net-backup.yml

The playook can be run to display the differences found between the saved config and the running config: 

    ansible-playbook --diff -i hosts net-backup.yml

The playook can be run with "net_backup_force=true to force the backup over an existing config to accept changes: 

    ansible-playbook --extra-vars "net_backup_force=true" -i hosts net-backup.yml


License
-------

GPL-3.0
