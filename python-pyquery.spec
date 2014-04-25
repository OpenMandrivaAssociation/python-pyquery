%define	module	pyquery

Summary:	JQuery-like library for Python

Name:		python-%{module}
Version:	1.2.8
Release:	1
Source0:	http://pypi.python.org/packages/source/p/pyquery/pyquery-%{version}.zip
License:	BSD
Group:		Development/Python
Url:		https://bitbucket.org/olauzanne/pyquery/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc *
%{py_puresitedir}/%{module}*



