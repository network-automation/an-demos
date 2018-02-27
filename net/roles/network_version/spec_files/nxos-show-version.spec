---
vars:
  net_version_data_item:
    system: "{{ item[0].version }}"
    firmware: "{{ item[1].version }}"
    poop: yes

keys:
  net_version_data:
    value: "{{ net_version_data_item }}"
    start_block: "^Cisco$"
    end_block: "^$"
    items:
      - "BIOS: version (?P<version>\\S+)"
      - "NXOS: version (?P<version>\\S+)"
