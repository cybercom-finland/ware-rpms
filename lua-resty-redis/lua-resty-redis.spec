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

Name:           lua-resty-redis
Version:        0.26
Release:        0.1%{?dist}
Summary:        Lua redis client driver for the ngx_lua based on the cosocket API

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/openresty/lua-resty-redis
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
This Lua library is a Redis client driver for the ngx_lua nginx module:

http://wiki.nginx.org/HttpLuaModule

This Lua library takes advantage of ngx_lua's cosocket API, which
ensures 100% nonblocking behavior.

%if 0%{?fedora} >= 20
%package compat
Summary:        Redis reply parser and request constructor library for Lua 5.1
Group:          Development/Libraries

%description compat
This Lua library is a Redis client driver for the ngx_lua nginx module:

http://wiki.nginx.org/HttpLuaModule

This Lua library takes advantage of ngx_lua's cosocket API, which
ensures 100% nonblocking behavior.
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
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
make %{?_smp_mflags} LIBDIR="%{_libdir}"

%if 0%{?fedora} >= 20
pushd %{lua51dir}
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
make %{?_smp_mflags} LIBDIR="%{_libdir}"
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
#%{lualibdir}/*.so
%{luapkgdir}/resty/redis*

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc README.markdown
#%{luacompatlibdir}/*.so
%{luacompatpkgdir}/resty/redis*
%endif


%changelog
* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.26-0.0
- 0.26

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.20-0.2
- fix build in F24

* Wed Feb 25 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 0.20-0.1
- fix build

