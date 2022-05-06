Name     : swayblur
Version  : 1.1.1
Release  : 1
URL      : https://github.com/WillPower3309/swayblur
Source   : https://github.com/WillPower3309/swayblur/archive/refs/tags/v%{version}.tar.gz
Summary  : Basic i3ipc based script to blur an output's wallpaper when a client is present in it
Group    : Development/Tools
License  : MIT
Requires: pypi-humanize-license = %{version}-%{release}
Requires: pypi-humanize-python = %{version}-%{release}
Requires: pypi-humanize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)


%description
Basic i3ipc based script to blur an output's wallpaper when a client is present in it.


%prep
%setup -q -n swayblur-%{version}


%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----


%files
%defattr(-,root,root,-)
/usr/lib/python3*/*
/usr/bin/swayblur
