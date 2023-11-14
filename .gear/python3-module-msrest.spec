%define pypi_name msrest

%def_without check

Name:    python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: The runtime library "msrest" for AutoRest generated Python clients
License: MIT
Group:   Development/Python3
URL:     https://github.com/AzureAD/microsoft-authentication-library-for-python

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-trio
BuildRequires: python3-module-requests
%endif


BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# Some tests require network connectivity, so they are skipped here.
%pyproject_run_pytest \
    --ignore=tests/asynctests/test_pipeline.py \
    --ignore=tests/asynctests/test_universal_http.py \
    --ignore=tests/test_auth.py \
    --ignore=tests/test_runtime.py


%files
%doc README.rst
%python3_sitelibdir/msrest/
%python3_sitelibdir/msrest-%version.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus
