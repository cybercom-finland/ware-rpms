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

Name:           lua-resty-core
Version:        0.1.14rc1
Release:        0.0%{?dist}
Summary:        New FFI-based Lua API for the ngx_lua module

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/openresty/%{name}
Source0:        https://github.com/openresty/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildarch:      noarch

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
New FFI-based Lua API for the ngx_lua module

%if 0%{?fedora} >= 20
%package compat
Summary:        New FFI-based Lua API for the ngx_lua module
Group:          Development/Libraries

%description compat
New FFI-based Lua API for the ngx_lua module
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

make install LUA_LIB_DIR=%{luapkgdir} DESTDIR=%{buildroot}

%if 0%{?fedora} >= 20
pushd %{lua51dir}
mkdir -p $RPM_BUILD_ROOT%{luacompatpkgdir}
mkdir -p $RPM_BUILD_ROOT%{luacompatlibdir}

make install LUA_LIB_DIR=%{luacompatpkgdir} DESTDIR=%{buildroot}
popd
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.markdown
#{lualibdir}/*.so
%{luapkgdir}/resty/core*
%{luapkgdir}/ngx/*.lua
%{luapkgdir}/ngx/ssl/*.lua

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc README.markdown
#{luacompatlibdir}/*.so
%{luacompatpkgdir}/resty/core*
%{luacompatpkgdir}/ngx/*.lua
%{luacompatpkgdir}/ngx/ssl/*.lua
%endif


%changelog
* Tue Mar 13 2018 Markus Linnala <Markus.Linnala@cybercom.com> - 0.1.14rc1-0.0
- 0.1.14rc1

* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.1.9-0.0
- 0.1.9

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.1.6-0.1
- fix build in F24

* Mon Jan 18 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.1.4-0.0
- update to 0.1.4

* Mon Mar  2 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 0.04-0.0
- initial


