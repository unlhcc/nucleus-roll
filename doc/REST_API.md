## Project Comet REST API Specification

* The **Content Type** of the API is JSON.  When making HTTP requests to this
  API you should specify the following headers:
    * Accept: application/json
    * Content-type: application/json
* A **Collection** is a group of Resources of a given type.
    * A **GET** request retrieves a list of summarized Resource representations
      This summary *may* include all or some of the Resource properties but
      *must* include a link to the full Resource representation.
    * A **POST** request will create a new Resource in the Collection. The set
      of Resource properties *must* be specified as a JSON object in the request
      body.
    * No other HTTP methods are supported for Collections
* A **Resource** is a representation of a singular object in the API (eg.
  Virtual Machine).
    * A **GET** request retrieves the full Resource representation.
    * A **DELETE** request will delete the Resource. This request *may* contain
      a JSON object which specifies optional parameters.
    * A **PUT** request is used to modify the properties of a Resource (eg.
      Change the name of a Virtual Machine). This kind of request *must not*
      alter the live state of the Resource. Only *actions* may alter live state.
    * A **POST** request commits an *action* upon a Resource (eg. Start a
      Virtual Machine). This request is made to a URI relative to the Resource
      URI. Available *actions* are described within the *actions* property of a
      Resource representation.  The request body *must* contain a JSON object
      which specifies parameters.
* URIs begin with a '/' to indicate the root of the API.
    * Variable segments in the URI begin with a ':' and should replaced with the
      appropriate resource identifier.

### Collection: Clusters

**URI:** /cluster

**Methods:**

* **GET**: Retrieve a summarized list of all project clusters
* **POST**: Create a new cluster

### Resource: Cluster

**URI:** /cluster/*:name*

**Methods:**

* **GET**: Retrieve the full description of a cluster
    * name: The name of the cluster.  Used to identify the cluster in this API
* **DELETE**: Remove the cluster
* **PUT**: update the parameters of existed cluster
* **POST**: *See cluster Actions*

**Actions (POST):**

* start: Start the whole cluster
* stop: Stop the whole cluster.

### Sub-collection: Virtual Machines

**URI:** /cluster/*:name*/vms

**Methods:**

* **GET**: Retrieve a summarized list of all defined Virtual Machines
* **POST**: Create a new Virtual Machine
    * name *(optional)*: The name of the VM.  Used to identify the VM in this
      API.  If omitted, a name will be chosen based on the template used.

### Sub-resource: Virtual Machine

**URI:** /cluster/*:name*/vms/*:name*

**Methods:**

* **GET**: Retrieve the full description of a Virtual Machine
    * name: The name of the VM.  Used to identify the VM in this API
    * state: Indicates the current state in the VM lifecycle
        * running: The VM is powered on
        * paused: The VMs virtual CPUs are paused
        * shutoff: The VM is powered off
    * memory: The amount of memory assigned to the VM (in MB)
    * cpus: The number of CPUs assigned to the VM
    * screenshot: A link to a recent capture of the screen in PNG format
* **DELETE**: Remove the Virtual Machine
* **PUT**: update the parameters of existed VM

* **POST**: *See Virtual Machine Actions*

**Actions (POST):**

* start: Power on a VM
* poweroff: Power off a VM forcefully. Note this action may produce undesirable
            results, for example unflushed disk cache in the guest.
* shutdown: Shut down a VM graceful. This action issue shutdown request to guest.
            And the guest will react this request. Note the guest OS may ignore
            the request.
* reset: Reset a VM immediately without the guest OS shutdown.
         It emulates the power reset button on a machine. Note that there is a
         risk of data loss caused by reset without the guest OS shutdown.
* stop: Shutdown a VM. When done, sync back the VM image to storage and remove the image from the host.

### Sub-resource: Virtual Machine Console

**URI:** /cluster/*:name*/vms/*:name*/console

Represents a console of the Virtual Machine.

**Methods:**

* **GET**: Redirect to the location of VM console


### Sub-collection: Virtual Machine storages
**URI:** /cluster/*:name*/vms/*:name*/storages
* **GET**: Retrieve a summarized list of all storages of specified guest
* **POST**: ?????? Attach a new storage or virtual drive to specified virtual machine.
    * pool: Storage pool which disk image file locate in.
    * vol: Storage volume name of disk image.

### Sub-resource: storage
**URI:** /cluster/*:name*/vms/*:name*/storages/*:zvol*
* **GET**: Retrieve storage information
    * dev: The name of the device.
    * dev: The name of the storage in the vm.
* **DELETE**: Remove the image from central storage.

**Actions (POST):**

* unmap: Detach the storage from VM, sync back if needed.

### Sub-collection: Virtual Machine Snapshots
**URI:** /cluster/*:name*/vms/*:name*/snapshots
* **GET**: Retrieve a list of snapshots on a VM.

### Sub-resource: Snapshot
**URI:** /cluster/*:name*/vms/*:name*/snapshots/*:snapshot*
* **GET**: Retrieve snapshot information.
    * created: The time when the snapshot was created
               (in seconds, since the epoch).
    * name: The snapshot name.
    * parent: The name of the parent snapshot, or an empty string if there is
              no parent.
* **POST**: See "Snapshot actions (POST)"

**Snapshot Actions (POST):**

* revert: Revert the domain to the given snapshot.

### Collection: Storage Pools

**URI:** /storagepools

**Methods:**

* **GET**: Retrieve a summarized list of all defined Storage Pools

### Resource: Storage Pool

**URI:** /storagepools/*:name*

**Methods:**

* **GET**: Retrieve the full description of a Storage Pool
    * name: The name of the Storage Pool
            Used to identify the Storage Pool in this API
    * state: Indicates the current state of the Storage Pool
        * active: The Storage Pool is ready for use
        * inactive: The Storage Pool is not available
    * path: The path of the defined Storage Pool
    * capacity: The total space which can be used to store volumes
                The unit is Bytes
    * allocated: The amount of space which is being used to store volumes
                The unit is Bytes
    * available: Free space available for creating new volumes in the pool

* **POST**: *See Storage Pool Actions*

**Actions (POST):**

* activate: Activate an inactive Storage Pool
* deactivate: Deactivate an active Storage Pool

### Collection: Storage Volumes

**URI:** /storagepools/*:poolname*/storagevolumes

**Methods:**

* **GET**: Retrieve a summarized list of all defined Storage Volumes
           in the defined Storage Pool
* **POST**: Create a new Storage Volume in the Storage Pool
            The return resource is a task resource * See Resource: Task *
            Only one of 'capacity', 'url' can be specified.
    * name: The name of the Storage Volume
    * capacity: The total space which can be used to store volumes
                The unit is Gbytes

### Resource: Storage Volume

**URI:** /storagepools/*:poolname*/storagevolumes/*:name*

**Methods:**

* **GET**: Retrieve the full description of a Storage Volume
    * name: The name of the Storage Volume
            Used to identify the Storage Volume in this API
    * state: mapped / unmapped
    * host: The name of the host
            where the image is attached to
    * zpool: The name of the zpool
            storing the zvol
    * target: name of iSCSI target if exists
    * capacity: The total space which can be used to store data
                The unit is Bytes


### Collection: Storage Servers

**URI:** /storageservers

**Methods:**

* **GET**: Retrieve a summarized list of used storage servers.

### Resource: Storage Server

**URI:** /storageservers/*:host*

**Methods:**

* **GET**: Retrieve description of a Storage Server
    * host: IP or host name of storage server

### Collection: Storage Targets

**URI:** /storageservers/*:name*/storagezpools

**Methods:**

* **GET**: Retrieve a list of available storage zpools
    * Response: A list with storage targets information.
        * host: IP or host name of storage server of this zpool.
        * zpool: Storage zpool name.
