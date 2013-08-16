CIMI Python Client
==================

This repository contains a simple [CIMI][cimi] client written in
python.  It currently allows you to interact with a CIMI server from
within a Python interpreter.  Eventually it will be expanded into a
full API that will also provide [Libcloud][libcloud] interoperability.


Building and Installing
-----------------------

The code is intended to be installed via pip and consequently the
build process will generate a pip distribution tarball.  To build the
package just run:

    $ mvn clean install

The package will appear in the subdirectory
`pypi/target/pypi-pkg/dist/`.

If you wish to run the defined tests, add the option `-DNOSETESTS` to
the above command.


Using the Client
----------------

To use the client, you must have access to a CIMI service.  With the
endpoint of that service, you can create a CloudEntryPoint instance:

    >>> from cimi.client.cloud_entry_point import CloudEntryPoint
    >>> cep = CloudEntryPoint('https://onehost-5.lal.in2p3.fr:8082/', ssl_verify=False)

The CloudEntryPoint, as in the specification, catalogs the types of
resources available and acts as the interface to a given CIMI cloud
infrastructure.  The object supports the following methods:

  * cep.show(): prints the CloudEntryPoint data to stdout
  * cep.keys(): provides the names (keys) of the resource collections
  * cep['collection']: returns Resource for given collection

It also supports the action methods shown below for Resource objects,
although typically only the 'edit' action will be supported for
CloudEntryPoints. 

All of the rest of the cloud resources are represented by Resource
objects.  These support:

  * r.show(): prints the CloudEntryPoint data to stdout
  * r.keys(): provides the names (keys) of the resource collections
  * r['collection']: returns Resource for given collection
  * r.do(action, data): performs the given actions
  * r.add(data): convenience method for r.do('add', data)
  * r.edit(data): convenience method for r.do('edit', data)
  * r.delete(): convenience method for r.do('delete', None)

To list the available collections and get the resource for one
particular collection, do the following:

    >>> cep.keys()
    [u'machineConfigs']
    >>> cfgs = cep['machineConfigs']

You can then list the available MachineConfiguration entries and get
the Resource object for one of them:

    >>> cfgs.keys()
    [u'MachineConfiguration/ed193d5b-ec5c-43ce-bcc9-6aa024eda322',
    u'MachineConfiguration/b9ef4f46-32e2-45e2-b6d4-01d2892212c4']
    >>> cfg = cfgs['MachineConfiguration/ed193d5b-ec5c-43ce-bcc9-6aa024eda322']

 You can then show the available operations for this entry and the
 contents: 

    >>> cfg.allowed_actions()
    [u'edit', u'delete']
    >>> 
    >>> cfg.show()
    {
         "cpu": 2, 
         "cpuArch": "x86_64", 
         "created": "2013-08-16T09:49:00.459Z", 
         "description": "great!", 
         "id": "MachineConfiguration/ed193d5b-ec5c-43ce-bcc9-6aa024eda322", 
         "memory": 2048, 
         "operations": [
             {
                 "href":
                 "MachineConfiguration/ed193d5b-ec5c-43ce-bcc9-6aa024eda322", 
                 "rel": "edit"
             }, 
             {
                 "href":
                 "MachineConfiguration/ed193d5b-ec5c-43ce-bcc9-6aa024eda322", 
                 "rel": "delete"
             }
         ], 
         "resourceURI":
         "http://schemas.dmtf.org/cimi/1/MachineConfiguration", 
         "updated": "2013-08-16T09:49:00.459Z"
    }
    >>>

You can then operate on this object by doing the following:

    >>> cfg.edit({'description': 'even greater!!'})
    200
    >>> 
    >>> cfg.delete()
    200
    >>>

Then reload the MachineConfiguration collection and see that the entry
we just deleted is gone.

    >>> cfgs.reload()
    >>> cfgs.keys()
    [u'MachineConfiguration/b9ef4f46-32e2-45e2-b6d4-01d2892212c4']
    >>> 


If resources define actions other than add, edit, or delete, they may
be executed with the more general 'do' method.


Feedback and Bug Reports
------------------------

This code is in an alpha state and quickly evolving along with the
StratusLab CIMI server.  Nonetheless, feedback on the code and its
functionality is appreciated; please send this feedback to the address
support@stratuslab.eu.  Specific bug reports can be provided via the
GitHub issues for this project. 


License
-------

Licensed under the Apache License, Version 2.0 (the "License"); you
may not use this file except in compliance with the License.  You may
obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.  See the License for the specific language governing
permissions and limitations under the License.

[cimi]: http://dmtf.org/sites/default/files/standards/documents/DSP0263_1.0.1.pdf
[libcloud]: http://libcloud.apache.org
