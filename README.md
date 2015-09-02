# SDSC "nucleus" roll

## Overview

This roll bundles... <REPLACE_ME> 

For more information about the various packages included in the nucleus roll please visit their official web pages:

- <a href="" target="_blank"></a> is .


## Requirements

To build/install this roll you must have root access to a Rocks development
machine (e.g., a frontend or development appliance).

If your Rocks development machine does *not* have Internet access you must
download the appropriate nucleus source file(s) using a machine that does
have Internet access and copy them into the `src/<package>` directories on your
Rocks development machine.


## Dependencies

The sdsc-roll must be installed on the build machine, since the build process
depends on make include files provided by that roll.

<IF APPROPRIATE>
The roll sources assume that modulefiles provided by SDSC compiler and mpi
rolls are available, but it will build without them as long as the environment
variables they provide are otherwise defined.
<ENDIF>

<IF APPROPRIATE>
The build process requires the XYZ libraries and assumes that the xyz
modulefile provided by the SDSC xyz-roll is available.  It will build without
the modulefile as long as the environment variables it provides are otherwise
defined.
<ENDIF>


## Building

To build the nucleus-roll, execute this on a Rocks development
machine (e.g., a frontend or development appliance):

```shell
% make 2>&1 | tee build.log
```

A successful build will create the file `nucleus-*.disk1.iso`.  If you built
the roll on a Rocks frontend, proceed to the installation step. If you built the
roll on a Rocks development appliance, you need to copy the roll to your Rocks
frontend before continuing with installation.

<IF APPROPRIATE>
This roll source supports building with different compilers and for different
MPI flavors.  The `ROLLCOMPILER` and `ROLLMPI` make variables can be used to
specify the names of compiler and MPI modulefiles to use for building the
software, e.g.,

```shell
make ROLLCOMPILER=intel ROLLMPI=mvapich2_ib 2>&1 | tee build.log
```

The build process recognizes "gnu", "intel" or "pgi" as the value for the
`ROLLCOMPILER` variable; any MPI modulefile name may be used as the value of
the `ROLLMPI` variable.  The default values are "gnu" and "rocks-openmpi".
<ENDIF>

<IF APPROPRIATE>
The roll supports specifying building with/for python versions other than
the one included with the o/s.  To use this feature, specify a `ROLLPY` make
variable that includes a space-delimited list of python modulefiles, e.g.,

```shell
% make ROLLPY=opt-python 2>&1 | tee build.log
```
<ENDIF>

<IF APPROPRIATE>
For gnu compilers, the roll supports a `ROLLOPTS` make variable value of
'avx' or 'avx2', indicating that the target architecture supports AVX/AVX2
instructions.
<ENDIF>


## Installation

To install, execute these instructions on a Rocks frontend:

```shell
% rocks add roll *.iso
% rocks enable roll nucleus
% cd /export/rocks/install
% rocks create distro
% rocks run roll nucleus | bash
```

In addition to the software itself, the roll installs nucleus environment
module files in:

```shell
/opt/modulefiles/applications/nucleus
```


## Testing

The nucleus-roll includes a test script which can be run to verify proper
installation of the roll documentation, binaries and module files. To
run the test scripts execute the following command(s):

```shell
% /root/rolltests/nucleus.t 
```

