%define	module	pyquery
%define name	python-%{module}
%define version	1.2.1
%define release 1

Summary:	jQuery-like library for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://bitbucket.org/olauzanne/pyquery/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-lxml >= 2.1
Requires:	python-cssselect
BuildRequires:	python-setuptools
BuildRequires:	python-lxml >= 2.1

%description
pyquery allows you to make jquery queries on xml documents.  The API
is as much as possible the similar to jquery. pyquery uses lxml for
fast xml and html manipulation.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%py_sitedir/%{module}*


%changelog
* Tue May 08 2012 Lev Givon <lev@mandriva.org> 1.2.1-1
+ Revision: 797583
- Update to 1.2.1.

* Sun Jan 15 2012 Lev Givon <lev@mandriva.org> 1.1.1-1
+ Revision: 760886
- imported package python-pyquery

