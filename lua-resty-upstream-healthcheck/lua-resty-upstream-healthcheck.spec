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

Name:           lua-resty-upstream-healthcheck
Version:        0.04
Release:        0.1
Summary:        Lua-land LRU Cache based on LuaJIT FFI

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/openresty/lua-resty-upstream-healthcheck
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
Health Checker for Nginx Upstream Servers in Pure Lua

%if 0%{?fedora} >= 20
%package compat
Summary:        Lua-land LRU Cache based on LuaJIT FFI for Lua 5.1
Group:          Development/Libraries

%description compat
in-Lua Health Checker for Nginx Upstream Servers on LuaJIT FFI
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
%{luapkgdir}/resty/upstream/*.lua

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc README.markdown
#{luacompatlibdir}/*.so
%{luacompatpkgdir}/resty/upstream/*.lua
%endif


%changelog
* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.04-0.1
- fix build in F24

* Mon Jan 18 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.03-0.0
- initial
