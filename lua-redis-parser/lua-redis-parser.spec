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

Name:           lua-redis-parser
Version:        0.12
Release:        0.1
Summary:        Redis reply parser and request constructor library for Lua

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/openresty/lua-redis-parser
Source0:        https://github.com/openresty/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
This lua library implements a thin and fast redis raw response parser
that constructs corresponding lua data strucutres, as well as a function
that constructs redis raw requests.

To maximize speed, this module is implemented in pure C.

This library is usually used by Lua code running atop lua-nginx-module
to access redis backends though redis2-nginx-module.

%if 0%{?fedora} >= 20
%package compat
Summary:        Redis reply parser and request constructor library for Lua 5.1
Group:          Development/Libraries

%description compat
This lua library implements a thin and fast redis raw response parser
that constructs corresponding lua data strucutres, as well as a function
that constructs redis raw requests.

To maximize speed, this module is implemented in pure C.

This library is usually used by Lua code running atop lua-nginx-module
to access redis backends though redis2-nginx-module.
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

make install LUA_LIB_DIR=%{lualibdir} DESTDIR=%{buildroot}

%if 0%{?fedora} >= 20
pushd %{lua51dir}
mkdir -p $RPM_BUILD_ROOT%{luacompatpkgdir}
mkdir -p $RPM_BUILD_ROOT%{luacompatlibdir}

make install LUA_LIB_DIR=%{luacompatlibdir} DESTDIR=%{buildroot}
popd
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.markdown
%{lualibdir}/redis/*.so
#{luapkgdir}/*.lua

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc README.markdown
%{luacompatlibdir}/redis/*.so
#{luacompatpkgdir}/*.lua
%endif


%changelog
* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.12-0.1
- fix build in F24

* Mon Jan 18 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.12-0.0
- update to 0.12

* Wed Feb 25 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 0.10-0.1
- fix build

