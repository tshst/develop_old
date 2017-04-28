gce-init
========

[![Build Status](https://travis-ci.org/kal3v/gce-init.svg?branch=master)](https://travis-ci.org/kal3v/gce-init)

Quickly create Google compute VM instances ready for other roles to be applied. Since the default standard persistent disk size is 10 GB, which may not be sufficient for everyone, a persistent disk with custom size may be created by the role.

Requirements
------------

 A Google service account with the _Compute Instance Admin_ and _Service Account Actor_ roles and its respective JSON key file.
 
The service account has to be activated. This can be accomplished with the `gcloud` tool: `gcloud auth activate-service-account [ACCOUNT] --key-file=KEY_FILE` (from [Cloud SDK documentation](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)). 

Role Variables
--------------

* `service_account_email` - The email of the service account
* `credentials_file` - Path to the JSON key file
* `machine_type` -  The GCE machine type, defaults to "n1-standard-1" (machine types can be found [here](https://cloud.google.com/compute/docs/machine-types))
* `image` - The GCE images, defaults to "debian-8" (image description can be found [here](https://cloud.google.com/compute/docs/images))
* `project_id` -  The GCE project ID (not the project name)
* `zone` - The GCE ressource zone, defaults to "europe-west1-b" (a list of the zones can be found [here](https://cloud.google.com/compute/docs/regions-zones/regions-zones))

If creating a persistent disk for each instance:

* `use_pd` - Create a persistent disk for each VM instance, defaults to "False"
* `disk_size` - The persistent disk size, defaults to "100" GB
* `disk_type` - The persistent disk type, defaults to "pd-ssd" (disk types can be found [here](https://cloud.google.com/compute/docs/disks/))


Example Playbook
----------------

Deploy a GCE instance VM and deploy PostgreSQL from source on it.

 _test.yml_:

    - hosts: localhost
      connection: local
      roles:
        - gce-init

    - hosts: gce_instances_ips
      become: yes
      become_method: sudo
      connection: ssh
      roles: 
        - postgresql-from-source

One way to do it on the command line is 

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook --extra-vars "service_account_email=service_account@project_id.iam.gserviceaccount.com credentials_file=project_name-dd969cfe12a2.json project_id=project_id instance_names=bunny,rex" test.yml
    
When creating persistent disks, just add `use_pd` and set the disk_size with the `disk_size` variable:

	ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook --extra-vars "service_account_email=ansible@pgperf-148515.iam.gserviceaccount.com credentials_file=pgperf-dd969cfe12a2.json project_id=pgperf-148515 instance_names=rex,bunny,t-bone use_pd=True disk_size=50 machine_type=n1-standard-1" --become test.yml -vv

Tests
-----

I've setup a GCE project and a service account for Travis to test the deployment of the VM instances. If you wish to implement such tests yourself, you will just need to encrypt a credentials file a the service account with the Travis CI command line tool, change the filename, project id and the service account name in [.travis.yml](.travis.yml) and in [tests/tests.yml](tests/test.yml).

License
-------

MIT
