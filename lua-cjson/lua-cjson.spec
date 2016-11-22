%if 0%{?fedora} >= 20

%if 0%{?fedora} < 24
%define luaver 5.2
%else
%define luaver 5.3
%endif

%else
%define luaver 5.1
%endif

%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define luacompatver 5.1
%define luacompatlibdir %{_libdir}/lua/%{luacompatver}
%define luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%define lua51dir %{_builddir}/lua51-%{name}-%{version}-%{release}

Name:           lua-cjson
Version:        2.1.0
Release:        0.2
Summary:        A fast JSON encoding/parsing module for Lua

Group:          Development/Libraries
License:        MIT
URL:            http://www.kyne.com.au/~mark/software/lua-cjson.php
Source0:        http://www.kyne.com.au/~mark/software/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  lua-devel
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires: lua(abi) = %{luaver}
%else
Requires: lua >= %{luaver}
%endif

%if 0%{?fedora} >= 20
BuildRequires:  compat-lua >= %{luacompatver}, compat-lua-devel >= %{luacompatver}
%endif


%description
The Lua CJSON module provides JSON support for Lua. It features:
- Fast, standards compliant encoding/parsing routines
- Full support for JSON with UTF-8, including decoding surrogate pairs
- Optional run-time support for common exceptions to the JSON specification
(infinity, NaN,..)
- No dependencies on other libraries

%if 0%{?fedora} >= 20
%package compat
Summary:        A fast JSON encoding/parsing module for Lua 5.1.
Group:          Development/Libraries

%description compat
The Lua CJSON module provides JSON support for Lua. It features:
- Fast, standards compliant encoding/parsing routines
- Full support for JSON with UTF-8, including decoding surrogate pairs
- Optional run-time support for common exceptions to the JSON specification
(infinity, NaN,..)
- No dependencies on other libraries
%endif

%prep
%setup -q
find . -name \*.[ch] -print -exec chmod -x '{}' \;

%if 0%{?fedora} >= 20
rm -rf %{lua51dir}
cp -a . %{lua51dir}
pushd %{lua51dir}
popd
%endif

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" LUA_INCLUDE_DIR=%{_includedir}

%if 0%{?fedora} >= 20
pushd %{lua51dir}
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" LUA_INCLUDE_DIR=%{_includedir}/lua-5.1
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
mkdir -p $RPM_BUILD_ROOT%{lualibdir}

make install DESTDIR="$RPM_BUILD_ROOT" LUA_CMODULE_DIR="%{lualibdir}"
make install-extra DESTDIR="$RPM_BUILD_ROOT" LUA_MODULE_DIR="%{luapkgdir}" \
        LUA_BIN_DIR="%{_bindir}"
rm -rf "$RPM_BUILD_ROOT""%{luapkgdir}"/cjson/tests


%if 0%{?fedora} >= 20
pushd %{lua51dir}
mkdir -p $RPM_BUILD_ROOT%{luacompatpkgdir}
mkdir -p $RPM_BUILD_ROOT%{luacompatlibdir}

make install DESTDIR="$RPM_BUILD_ROOT" LUA_CMODULE_DIR="%{luacompatlibdir}"
make install-extra DESTDIR="$RPM_BUILD_ROOT" LUA_MODULE_DIR="%{luacompatpkgdir}" \
        LUA_BIN_DIR="%{_bindir}"
rm -rf "$RPM_BUILD_ROOT""%{luacompatpkgdir}"/cjson/tests
popd
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE NEWS performance.html performance.txt manual.html manual.txt rfc4627.txt THANKS
%{lualibdir}/*
%{luapkgdir}/*
%{_bindir}/*

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc LICENSE NEWS performance.html performance.txt manual.html manual.txt rfc4627.txt THANKS
%{luacompatlibdir}/*
%{luacompatpkgdir}/*
%endif


%changelog
* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 2.1.0-0.2
- fix build in F24

* Mon Mar  2 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 2.1.0-0.1
- fix compat-lua build to use proper LUA_INCLUDE_DIR
- use -fPIC when building

* Wed Feb 25 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 2.1.0-0.0
- initial
