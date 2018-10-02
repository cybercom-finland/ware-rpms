Name:           brotli
Version:        1.0.3
Release:        0.0%{?dist}
Summary:        Lossless compression algorithm

License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++ gcc cmake
%if 0%{?rhel}
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel python3-devel
%endif

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n python2-%{name}
Summary:        Lossless compression algorithm (python 2)
%if 0%{?rhel}
Requires: python
Obsoletes: python-%{name}
%else
Requires: python2
%{?python_provide:%python_provide python2-%{name}}
%endif

%description -n python2-%{name}
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs a Python 2 module.


%if 0%{?rhel}
%else
%package -n python3-%{name}
Requires: python3
Summary:        Lossless compression algorithm (python 3)
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs a Python 3 module.
%endif

%package -n %{name}-devel
Summary:        Lossless compression algorithm (development files)
Requires: %{name}%{?_isa} = %{version}-%{release} 

%description -n %{name}-devel
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs the development files

%prep
%autosetup
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
%{__chmod} 644 c/enc/*.[ch]
%{__chmod} 644 c/include/brotli/*.h
%{__chmod} 644 c/tools/brotli.c
%build

mkdir -p build
cd build
%cmake .. -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%make_build
cd ..
%py2_build
%if 0%{?rhel}
%else
%py3_build
%endif

%install
cd build
%make_install

# I couldn't find the option to not build the static libraries
%__rm "%{buildroot}%{_libdir}/"*.a

cd ..
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default. If, however, we're installing separate
# executables for python2 and python3, the order needs to be reversed so
# the unversioned executable is the python2 one.
%py2_install
%if 0%{?rhel}
%else
%py3_install
%endif
%{__install} -dm755 "%{buildroot}%{_mandir}/man3"
cd docs
for i in *.3;do
%{__install} -m644 "$i" "%{buildroot}%{_mandir}/man3/${i}brotli"
done

%ldconfig_scriptlets

%check
cd build
ctest -V
cd ..
%if 0%{?rhel}
%else
# Older pythons distutils do not know distribution option: test_suite
%{__python2} setup.py test
%{__python3} setup.py test
%endif

%files
%{_bindir}/brotli
%{_libdir}/*.so.*
%license LICENSE

# Note that there is no %%files section for the unversioned python module
# if we are building for several python runtimes
%files -n python2-%{name}
%{python2_sitearch}/*
%license LICENSE

%if 0%{?rhel}
%else
%files -n python3-%{name}
%{python3_sitearch}/*
%license LICENSE
%endif

%files -n %{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*


%changelog
* Mon Mar 19 2018 Markus Linnala <Markus.Linnala@cybercom.com> - 1.0.3-0.0
- build for rhel too

* Fri Mar 02 2018 Travis Kendrick <pouar@pouar.net> - 1.0.3-1
- update to 1.0.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Switch to %%ldconfig_scriptlets

* Fri Sep 22 2017 Travis Kendrick <pouar@pouar.net> - 1.0.1-1
- update to 1.0.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-4
- add man pages

* Sun May 14 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-3
- wrong directory for ctest
- LICENSE not needed in -devel
- fix "spurious-executable-perm"
- rpmbuild does the cleaning for us, so 'rm -rf %%{buildroot}' isn't needed

* Sat May 13 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-2
- include libraries and development files

* Sat May 06 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-1
- Initial build
