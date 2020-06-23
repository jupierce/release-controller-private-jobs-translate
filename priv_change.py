#!/usr/bin/python3

import glob
import oyaml as yaml
import os

#~/go/src/github.com/openshift/release/core-services/release-controller/_releases/priv [cve_workflow|●1✚ 2…29⚑ 1]
#19:19 $ for j in *.json; do cat ${j} | jq '.verify | keys[] as $k | (.[$k] | .prowJob.name)'; done | uniq | tr '\n' ','
# "priv-release-openshift-ocp-installer-e2e-aws-4.1","priv-release-openshift-ocp-installer-e2e-aws-serial-4.1","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-aws-4.2","priv-release-openshift-ocp-installer-console-aws-4.2","priv-release-openshift-ocp-installer-e2e-aws-serial-4.2","priv-release-openshift-ocp-installer-e2e-aws-upi-4.2","priv-release-openshift-ocp-installer-e2e-azure-4.2","priv-release-openshift-ocp-installer-e2e-azure-serial-4.2","priv-release-openshift-ocp-installer-e2e-gcp-4.2","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.2","priv-release-openshift-ocp-installer-e2e-metal-4.2","priv-release-openshift-ocp-installer-e2e-metal-serial-4.2","priv-release-openshift-ocp-installer-e2e-openstack-4.2","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.2","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.2","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.2","priv-release-openshift-ocp-installer-e2e-aws-4.3","priv-release-openshift-ocp-installer-console-aws-4.3","priv-release-openshift-ocp-installer-e2e-aws-fips-4.3","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.3","priv-release-openshift-ocp-installer-e2e-aws-serial-4.3","priv-release-openshift-ocp-installer-e2e-aws-upi-4.3","priv-release-openshift-ocp-installer-e2e-azure-4.3","priv-release-openshift-ocp-installer-e2e-azure-serial-4.3","priv-release-openshift-ocp-installer-e2e-gcp-4.3","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.3","priv-release-openshift-ocp-installer-e2e-metal-4.3","priv-release-openshift-ocp-installer-e2e-metal-serial-4.3","priv-release-openshift-ocp-installer-e2e-openstack-4.3","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.3","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.3","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.3","priv-release-openshift-ocp-installer-e2e-aws-4.4","priv-release-openshift-ocp-installer-console-aws-4.4","priv-release-openshift-ocp-installer-e2e-aws-fips-4.4","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.4","priv-release-openshift-ocp-installer-e2e-aws-serial-4.4","priv-release-openshift-ocp-installer-e2e-aws-upi-4.4","priv-release-openshift-ocp-installer-e2e-azure-4.4","priv-release-openshift-ocp-installer-e2e-azure-serial-4.4","priv-release-openshift-ocp-installer-e2e-gcp-4.4","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.4","priv-release-openshift-ocp-installer-e2e-metal-4.4","priv-periodic-ci-openshift-release-master-ocp-4.4-e2e-metal-ipi","priv-release-openshift-ocp-installer-e2e-metal-serial-4.4","priv-release-openshift-ocp-installer-e2e-openstack-4.4","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.4","priv-release-openshift-ocp-installer-e2e-ovirt-4.4","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.4","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.4","priv-release-openshift-ocp-installer-e2e-aws-4.5","priv-release-openshift-ocp-installer-console-aws-4.5","priv-release-openshift-ocp-installer-e2e-aws-fips-4.5","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.5","priv-release-openshift-ocp-installer-e2e-aws-serial-4.5","priv-release-openshift-ocp-installer-e2e-aws-upi-4.5","priv-release-openshift-ocp-installer-e2e-azure-4.5","priv-release-openshift-ocp-installer-e2e-azure-serial-4.5","priv-release-openshift-ocp-installer-e2e-gcp-4.5","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.5","priv-release-openshift-ocp-installer-e2e-metal-4.5","priv-periodic-ci-openshift-release-master-ocp-4.5-e2e-metal-ipi","priv-release-openshift-ocp-installer-e2e-metal-serial-4.5","priv-release-openshift-ocp-installer-e2e-ovirt-4.5","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.5","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.5","priv-release-openshift-ocp-installer-e2e-aws-4.6","priv-periodic-ci-openshift-release-master-ocp-4.6-e2e-metal-ipi","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-aws-4.7","priv-release-openshift-origin-installer-e2e-aws-upgrade",

req_names = set(["priv-release-openshift-ocp-installer-e2e-aws-4.1","priv-release-openshift-ocp-installer-e2e-aws-serial-4.1","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-aws-4.2","priv-release-openshift-ocp-installer-console-aws-4.2","priv-release-openshift-ocp-installer-e2e-aws-serial-4.2","priv-release-openshift-ocp-installer-e2e-aws-upi-4.2","priv-release-openshift-ocp-installer-e2e-azure-4.2","priv-release-openshift-ocp-installer-e2e-azure-serial-4.2","priv-release-openshift-ocp-installer-e2e-gcp-4.2","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.2","priv-release-openshift-ocp-installer-e2e-metal-4.2","priv-release-openshift-ocp-installer-e2e-metal-serial-4.2","priv-release-openshift-ocp-installer-e2e-openstack-4.2","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.2","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.2","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.2","priv-release-openshift-ocp-installer-e2e-aws-4.3","priv-release-openshift-ocp-installer-console-aws-4.3","priv-release-openshift-ocp-installer-e2e-aws-fips-4.3","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.3","priv-release-openshift-ocp-installer-e2e-aws-serial-4.3","priv-release-openshift-ocp-installer-e2e-aws-upi-4.3","priv-release-openshift-ocp-installer-e2e-azure-4.3","priv-release-openshift-ocp-installer-e2e-azure-serial-4.3","priv-release-openshift-ocp-installer-e2e-gcp-4.3","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.3","priv-release-openshift-ocp-installer-e2e-metal-4.3","priv-release-openshift-ocp-installer-e2e-metal-serial-4.3","priv-release-openshift-ocp-installer-e2e-openstack-4.3","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.3","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.3","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.3","priv-release-openshift-ocp-installer-e2e-aws-4.4","priv-release-openshift-ocp-installer-console-aws-4.4","priv-release-openshift-ocp-installer-e2e-aws-fips-4.4","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.4","priv-release-openshift-ocp-installer-e2e-aws-serial-4.4","priv-release-openshift-ocp-installer-e2e-aws-upi-4.4","priv-release-openshift-ocp-installer-e2e-azure-4.4","priv-release-openshift-ocp-installer-e2e-azure-serial-4.4","priv-release-openshift-ocp-installer-e2e-gcp-4.4","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.4","priv-release-openshift-ocp-installer-e2e-metal-4.4","priv-periodic-ci-openshift-release-master-ocp-4.4-e2e-metal-ipi","priv-release-openshift-ocp-installer-e2e-metal-serial-4.4","priv-release-openshift-ocp-installer-e2e-openstack-4.4","priv-release-openshift-ocp-installer-e2e-openstack-serial-4.4","priv-release-openshift-ocp-installer-e2e-ovirt-4.4","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.4","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.4","priv-release-openshift-ocp-installer-e2e-aws-4.5","priv-release-openshift-ocp-installer-console-aws-4.5","priv-release-openshift-ocp-installer-e2e-aws-fips-4.5","priv-release-openshift-ocp-installer-e2e-aws-ovn-4.5","priv-release-openshift-ocp-installer-e2e-aws-serial-4.5","priv-release-openshift-ocp-installer-e2e-aws-upi-4.5","priv-release-openshift-ocp-installer-e2e-azure-4.5","priv-release-openshift-ocp-installer-e2e-azure-serial-4.5","priv-release-openshift-ocp-installer-e2e-gcp-4.5","priv-release-openshift-ocp-installer-e2e-gcp-serial-4.5","priv-release-openshift-ocp-installer-e2e-metal-4.5","priv-periodic-ci-openshift-release-master-ocp-4.5-e2e-metal-ipi","priv-release-openshift-ocp-installer-e2e-metal-serial-4.5","priv-release-openshift-ocp-installer-e2e-ovirt-4.5","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-vsphere-upi-4.5","priv-release-openshift-ocp-installer-e2e-vsphere-upi-serial-4.5","priv-release-openshift-ocp-installer-e2e-aws-4.6","priv-periodic-ci-openshift-release-master-ocp-4.6-e2e-metal-ipi","priv-release-openshift-origin-installer-e2e-aws-upgrade","priv-release-openshift-ocp-installer-e2e-aws-4.7","priv-release-openshift-origin-installer-e2e-aws-upgrade",])
used_names = set()

def run():
    periodics_buffer = []
    periodic_buffer = []
    for filepath in glob.glob('/home/jupierce/go/src/github.com/openshift/release/ci-operator/jobs/openshift/release/*.yaml'):
        filename = os.path.basename(filepath)

        with open(filepath, 'r') as f:
            lines = f.readlines()

            print(f'Processing: {filepath}')

            if 'periodics:\n' not in lines:
                print(f'No periodics found..')
                continue

            in_periodics = False
            with open('priv-'+filename, 'w+') as out:

                def write_periodics_buffer():
                    nonlocal periodics_buffer
                    nonlocal periodic_buffer

                    if periodic_buffer:
                        periodics_buffer.append(periodic_buffer)
                        periodic_buffer = []

                    if not periodics_buffer:
                        return

                    for buffer in periodics_buffer:

                        prowjob_name = ''
                        for line in buffer:
                            if line.startswith('  name:'):
                                prowjob_name = line.split(':', 1)[1].strip()

                        priv_prowjob_name = f'priv-{prowjob_name}'
                        if priv_prowjob_name not in req_names:
                            print(f'EXCLUDING: {prowjob_name}')
                            continue

                        used_names.add(priv_prowjob_name)

                        for line in buffer:
                            if 'agent: kubernetes' in line:
                                out.write(line)
                                out.write('  hidden: true\n')
                            elif line.startswith('  name:'):
                                out.write(f'  name: {priv_prowjob_name}\n')
                            elif line.startswith('  cron:'):
                                out.write('  cron: @yearly\n')
                            else:
                                out.write(line)
                    periodics_buffer = []

                for lineno, line in enumerate(lines):

                    if line.startswith('periodics:'):
                        in_periodics = True
                        out.write(line)
                        continue
                    elif line.strip() and not line.startswith((' ', '-')):
                        print(f'BREAKING!: {ord(line[0])}')
                        in_periodics = False
                        write_periodics_buffer()
                        out.write(line)
                        continue

                    if not in_periodics:
                        out.write(line)
                    else:
                        if line.startswith('-'):
                            if periodic_buffer:
                                periodics_buffer.append(periodic_buffer)
                                periodic_buffer = []
                        periodic_buffer.append(line)

                write_periodics_buffer()

    print(f'Found missing required names: {req_names.difference(used_names)}')

run()
