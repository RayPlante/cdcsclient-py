# cdcsclient-py

A python implementation of a client that can access a remote CDCS
server via its web API.

This repository provides a python package that is intended to be
complete and knowledgeable client to the Configurable Data Curation
System (CDCS) v2.0 web service API.  That is, it presents the low-level
semantics of the web API in a python programming interface.
Currently, this software is _experimental_ and, thus, not expected to be
complete at this time.

## Prerequisites

This software requires Python 2.7.9 or Python 3.4 or greater.  

The python module prerequisites are captured in the `requirements.txt`
file.  The prerequisites include:

  * requests (> 2.18.0)

These can be installed using the [`pip`](https://pip.pypa.io/) tool:

```
  pip install -r requirements.txt
```

## Building or Installing the Package

To build this package, use the included `setup.py` script:

```
  python setup.py build
```

This installs the compiled Python code into a subdirectory called
`build`.  To install the package, use the `install` command:

```
  python setup.py install
```

Use the `--prefix` option to install the package in a specific
location (see `setuptools` documentation for details).

## Running the Unit Tests

The unit tests can be executed via the included `setup.py` script:

```
  python setup.py test
```

## Disclaimer

This repository serves as a platform for open community collaboration
to enable and encourage greater sharing of and interoperability
between research data from around the world. Except where otherwise
noted, the content and software within this repository should be
considered a work in progress, may contain input from non-governmental
contributors, and thus should not be construed to represent the
position nor have the endorsement the United States government.

This software was developed (possibly in part) by employees of the
National Institute of Standards and Technology (NIST), an agency of
the Federal Government and is being made available as a public
service. Pursuant to title 17 United States Code Section 105, works of
NIST employees are not subject to copyright protection in the United
States.  This software may be subject to foreign copyright.
Permission in the United States and in foreign countries, to the
extent that NIST may hold copyright, to use, copy, modify, create
derivative works, and distribute this software and its documentation
without fee is hereby granted on a non-exclusive basis, provided that
this notice and disclaimer of warranty appears in all copies.

THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND,
EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED
TO, ANY WARRANTY THAT THE SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE, AND FREEDOM FROM INFRINGEMENT, AND ANY WARRANTY THAT THE
DOCUMENTATION WILL CONFORM TO THE SOFTWARE, OR ANY WARRANTY THAT THE
SOFTWARE WILL BE ERROR FREE.  IN NO EVENT SHALL NIST BE LIABLE FOR ANY
DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT, INDIRECT, SPECIAL OR
CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR IN ANY WAY
CONNECTED WITH THIS SOFTWARE, WHETHER OR NOT BASED UPON WARRANTY,
CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS SUSTAINED BY
PERSONS OR PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS
SUSTAINED FROM, OR AROSE OUT OF THE RESULTS OF, OR USE OF, THE
SOFTWARE OR SERVICES PROVIDED HEREUNDER. 
