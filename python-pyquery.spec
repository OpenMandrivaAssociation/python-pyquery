%define	module	pyquery

Summary:	JQuery-like library for Python

Name:		python-%{module}
Version:	2.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/e4/46/596311bb390c902b61499ff9fd5a355cdf85c8455737cb0f08c6c2c13e22/pyquery-2.1.0.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://bitbucket.org/olauzanne/pyquery/
BuildArch:	noarch
Requires:	python%{pyver}dist(lxml) >= 2.1
Requires:	python%{pyver}dist(cssselect)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(lxml) >= 2.1

%description
pyquery allows you to make jquery queries on xml documents.  The API
is as much as possible the similar to jquery. pyquery uses lxml for
fast xml and html manipulation.

%prep
%setup -q -n pyquery-2.1.0

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc *
%{py_puresitedir}/%{module}*



