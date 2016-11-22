# run get.sh and then update these
%define gitrev 211
%define githash 5db62dc

%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif


Name:           brotli
Version:        0.4.0
Release:        104.1.%{gitrev}
Summary:        Brotli compression format

License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}.tar.gz#/google-%{name}-v%{version}-%{gitrev}-g%{githash}.tar.gz
Patch1:         0001-add-.cc-files-too-to-lib.patch
Patch2:         0002-handle-deps-better-with.patch
Patch3:         0003-tests-remove-created-test-files.patch
Patch4:         0004-tests-limit-test-files-more-strictly.patch

BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
BuildRequires:  python3-devel
%endif
%if 0%{?fedora} >= 25
BuildRequires:  perl
%endif

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

This package installs a command line utility.


%package        -n python-brotli
Summary:        Brotli compression format

%description    -n python-brotli
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

This package installs a Python 2 module.


%if 0%{?rhel} && 0%{?rhel} <= 7
%else
%package        -n python3-brotli
Summary:        Brotli compression format

%description    -n python3-brotli
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

This package installs a Python 3 module.
%endif

%package devel
Summary:        Brotli compression format

%description    devel
Brotli devel

%package docs
Summary:        Brotli docs

%description docs
Brotli docs

%prep
%setup -q -n google-brotli-%{githash}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp -a tests tests.orig

%build
%if 0%{?rhel} && 0%{?rhel} <= 7
%{__python} setup.py build
%else
%py2_build
%py3_build
%endif

%{make_build} CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="-pie" all

%install
%if 0%{?rhel} && 0%{?rhel} <= 7
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%else
%py2_install
%py3_install
%endif
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 bin/bro $RPM_BUILD_ROOT/%{_bindir}/brotli
mkdir -p $RPM_BUILD_ROOT/%{_libdir}

for a in enc dec common; do
  mkdir -p $RPM_BUILD_ROOT/%{_includedir}/brotli/"$a"
  perl -pi -e 's,\#include \"\.\./common/(.*?)\",#include <brotli/common/$1>,' "$a"/*.h
  perl -pi -e 's,\#include \"\./(.*?)\",#include <brotli/'"$a"'/$1>,' "$a"/*.h
  install -m 0644 "$a"/*.h $RPM_BUILD_ROOT/%{_includedir}/brotli/"$a"/
done
install -m 0644 include/brotli/*.h $RPM_BUILD_ROOT/%{_includedir}/brotli/

install -m 0644 libbrotli.a $RPM_BUILD_ROOT/%{_libdir}/

%check
%if 0%{?rhel} && 0%{?rhel} <= 7
rm -rf tests
cp -a tests.orig tests
%{__python} setup.py test
%else
# It does not clean tests directory properly after run so next test fails
rm -rf tests
cp -a tests.orig tests
%{__python2} setup.py test
rm -rf tests
cp -a tests.orig tests
%{__python3} setup.py test
%endif

%files
%doc README.md
%{_bindir}/brotli

%files -n python-brotli
%doc README.md
%license LICENSE
%if 0%{?rhel} && 0%{?rhel} <= 7
%{python_sitearch}/*
%else
%{python2_sitearch}/*

%files -n python3-brotli
%doc README.md
%license LICENSE
%{python3_sitearch}/*
%endif

%files devel
%license LICENSE
%{_includedir}/brotli/*.h
%{_includedir}/brotli/*/*.h
%{_libdir}/*.a

%files docs
%license LICENSE
%doc README.md docs/*

%changelog
* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-104.1.211
- add public includes

* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-104.0.211
- 0.4.0 gitrev 211

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-103.1.102
- fix rhel rules in spec

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-103.0.102
- build only libbrotli.a
- fix Makefile

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-102.0.102
- update to gitrev 102

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-101.1.75
- fix includes again

* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-101.0.75
- fix includes

* Thu Jun 30 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.4.0-100.0.75
- 0.4.0
- add brotli-docs package

* Thu Apr 14 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.3.0-100.0.69
- for RHEL-7

* Sat Mar 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.3.0-1
- update to latest version

* Wed Sep 23 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.2.0-1
- First build
