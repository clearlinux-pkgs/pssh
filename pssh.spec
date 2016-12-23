#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pssh
Version  : 2.3.1
Release  : 8
URL      : https://parallel-ssh.googlecode.com/files/pssh-2.3.1.tar.gz
Source0  : https://parallel-ssh.googlecode.com/files/pssh-2.3.1.tar.gz
Summary  : Parallel version of OpenSSH and related tools
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pssh-bin
Requires: pssh-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package bin
Summary: bin components for the pssh package.
Group: Binaries

%description bin
bin components for the pssh package.


%package python
Summary: python components for the pssh package.
Group: Default

%description python
python components for the pssh package.


%prep
%setup -q -n pssh-2.3.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/man/man1/pnuke.1
/usr/man/man1/prsync.1
/usr/man/man1/pscp.1
/usr/man/man1/pslurp.1
/usr/man/man1/pssh.1

%files bin
%defattr(-,root,root,-)
/usr/bin/pnuke
/usr/bin/prsync
/usr/bin/pscp
/usr/bin/pslurp
/usr/bin/pssh
/usr/bin/pssh-askpass

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
