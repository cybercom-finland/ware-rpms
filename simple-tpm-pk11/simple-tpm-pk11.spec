%define git_num 15
%define git_rev 6a0188a

Summary:	A simple tool for using the TPM chip to secure SSH keys
Name:		simple-tpm-pk11
Version:	0.06
Release:	1.0%{?dist}
License:	ASL 2.0
URL:		https://github.com/ThomasHabets/%{name}/
# wget --no-check-certificate --content-disposition -q -nv -c  https://github.com/ThomasHabets/simple-tpm-pk11/tarball/master
Source:		https://github.com/ThomasHabets/%{name}/archive/ThomasHabets-%{name}-%{version}-%{git_num}-g%{git_rev}.tar.gz

BuildRequires: opencryptoki-devel
BuildRequires: openssl-devel
BuildRequires: trousers-devel

# used by bootstrap.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

Requires: tpm-tools

%description
A simple tool for using the TPM chip to secure SSH keys.

%prep
%autosetup -n ThomasHabets-%{name}-%{git_rev}

%build
./bootstrap.sh
%configure --disable-static
%make_build
pushd check-srk
g++ -o check-srk -std=gnu++11 check-srk.cc -ltspi -lssl -lcrypto
popd
%install
%make_install
find %{buildroot} -type f -name '*.la' -delete
install -d %{buildroot}%{_libexecdir}/simple-tpm-pk11/
install -m755 check-srk/check-srk %{buildroot}%{_libexecdir}/simple-tpm-pk11/

%files
%license LICENSE
%doc FAQ README.md TPM-TROUBLESHOOTING
%{_bindir}/stpm-*
%{_libdir}/libsimple-tpm-pk11.so*
%{_libexecdir}/simple-tpm-pk11/check-srk
%{_mandir}/man1/stpm-*.1*
%{_mandir}/man7/simple-tpm-pk11.7*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Tue Oct  2 2018 Markus Linnala <Markus.Linnala@cybercom.com> - 0.06-1.0
- add check-srk

* Tue Oct  2 2018 Markus Linnala <Markus.Linnala@cybercom.com> - 0.06-0.0
- Initial version
