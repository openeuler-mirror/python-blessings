%global upstream_name blessings


Name:           python-%{upstream_name}
Version:        1.7
Release:        1
Summary:        Python library for terminal coloring, styling, and positioning
License:        MIT
URL:            https://github.com/erikrose/blessings
Source0:        https://files.pythonhosted.org/packages/source/b/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# https://github.com/erikrose/blessings/issues/25
Patch1:         0001-fix-tests-when-run-without-a-tty-fixes-25.patch
Patch2:         0002-more-fixes-for-tests-without-a-tty.patch
BuildArch:      noarch

%description
Blessings is a thin, practical wrapper around terminal coloring, styling, and 
positioning in Python.

%package -n python3-%{upstream_name}
Summary:        Python 3 library for terminal coloring, styling, and positioning
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{upstream_name}
Blessings is a thin, practical wrapper around terminal coloring, styling, and 
positioning in Python.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch1 -p1
%patch2 -p1
rm -rf blessings.egg-info

%build
%py3_build

%install
%py3_install

%check
nosetests-3 build/lib

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/blessings
%{python3_sitelib}/blessings*.egg-info

%changelog
* Wed June 30 2021 liuliang <liuliang1@kylinos.cn> - 1.7-1
- Package init
