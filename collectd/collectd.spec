%global _hardened_build 1
%global __provides_exclude_from ^%{_libdir}/collectd/.*\\.so$

Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 5.6.2
Release: 0.3%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: https://collectd.org/

Source: https://collectd.org/files/%{name}-%{version}.tar.bz2
Source1: collectd-httpd.conf
#Source2: collectd.service
Source91: apache.conf
Source92: email.conf
Source93: mysql.conf
Source94: nginx.conf
Source95: sensors.conf
Source96: snmp.conf
Source97: rrdtool.conf

Patch0: %{name}-include-collectd.d.patch

%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%endif

BuildRequires: libtool-ltdl-devel
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires: perl-devel
%endif
%if 0%{?fedora} >= 25
BuildRequires: perl-generators
%endif
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed)
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires: python-devel
%endif
BuildRequires: libgcrypt-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%endif

Obsoletes: collectd-disk == 5.6.1.7.g9c962b9
Obsoletes: collectd-python == 5.6.1.7.g9c962b9

%description
collectd is a daemon which collects system performance statistics periodically
and provides mechanisms to store the values in a variety of ways,
for example in RRD files.

%package amqp
Summary:       AMQP plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel
%description amqp
This plugin can be used to communicate with other instances of collectd
or third party applications using an AMQP message broker.


%package apache
Summary:       Apache plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description apache
This plugin collects data provided by Apache's 'mod_status'.


%package ascent
Summary:       Ascent plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description ascent
This plugin collects data about an Ascent server,
a free server for the "World of Warcraft" game.


%package bind
Summary:       Bind plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description bind
This plugin retrieves statistics from the BIND dns server.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package ceph
Summary:       Ceph plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: yajl-devel
%description ceph
This plugin collects data from Ceph.
%endif


%package chrony
Summary:       Chrony plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description chrony
Chrony plugin for collectd


%package curl
Summary:       Curl plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description curl
This plugin reads webpages with curl


%if 0%{?fedora} || 0%{?rhel} >= 6
%package curl_json
Summary:       Curl JSON plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: yajl-devel
%description curl_json
This plugin retrieves JSON data via curl.
%endif


%package curl_xml
Summary:       Curl XML plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description curl_xml
This plugin retrieves XML data via curl.


%package dbi
Summary:       DBI plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdbi-devel
%description dbi
This plugin uses the dbi library to connect to various databases,
execute SQL statements and read back the results.


%if 0%{?fedora} || 0%{?rhel} >= 6
%package dns
Summary:       DNS traffic analysis plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpcap-devel
%description dns
This plugin collects DNS traffic data.
%endif


%package drbd
Summary:       DRBD plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description drbd
This plugin collects data from DRBD.


%package email
Summary:       Email plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description email
This plugin collects data provided by spamassassin.


%package generic-jmx
Summary:       Generic JMX plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description generic-jmx
This plugin collects data provided by JMX.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package gmond
Summary:       Gmond plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: ganglia-devel
%description gmond
This plugin receives multicast traffic sent by gmond,
the statistics collection daemon of Ganglia.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package gps
Summary:       GPS plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: gpsd-devel
%description gps
This plugin monitor gps related data through gpsd.
%endif


%package ipmi
Summary:       IPMI plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: OpenIPMI-devel
%description ipmi
This plugin for collectd provides IPMI support.


%if 0%{?fedora} || 0%{?rhel} >= 6
%package iptables
Summary:       Iptables plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: iptables-devel
%description iptables
This plugin collects data from iptables counters.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package ipvs
Summary:       IPVS plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description ipvs
This plugin collects data from IPVS.
%endif


%package java
Summary:       Java bindings for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires: java-1.8.0-openjdk-devel
%else
BuildRequires: java-1.7.0-openjdk-devel
%endif
BuildRequires: jpackage-utils
%description java
These are the Java bindings for collectd.


%package lua
Summary:       Lua plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lua-devel
%description lua
The Lua plugin embeds a Lua interpreter into collectd and exposes the
application programming interface (API) to Lua scripts.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package lvm
Summary:       LVM plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lvm2-devel
%description lvm
This plugin collects information from lvm
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package modbus
Summary:       Modbus plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmodbus-devel
%description modbus
This plugin connects to a Modbus "slave" via Modbus/TCP
and reads register values.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package mqtt
Summary:       MQTT plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mosquitto-devel
%description mqtt
The MQTT plugin publishes and subscribes to MQTT topics.
%endif


%package mysql
Summary:       MySQL plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mysql-devel
%description mysql
MySQL querying plugin. This plugin provides data of issued commands,
called handlers and database traffic.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package netlink
Summary:       Netlink plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: iproute-static, libmnl-devel
%description netlink
This plugin uses a netlink socket to query the Linux kernel
about statistics of various interface and routing aspects.
%endif


%package nginx
Summary:       Nginx plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description nginx
This plugin collects data provided by Nginx.


%if 0%{?fedora} || 0%{?rhel} >= 6
%package notify_desktop
Summary:       Notify desktop plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libnotify-devel
%description notify_desktop
This plugin sends a desktop notification to a notification daemon,
as defined in the Desktop Notification Specification.
%endif


%package notify_email
Summary:       Notify email plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libesmtp-devel
%description notify_email
This plugin uses the ESMTP library to send
notifications to a configured email address.


%ifnarch s390 s390x
%package nut
Summary:       Network UPS Tools plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: nut-devel
%description nut
This plugin for collectd provides Network UPS Tools support.
%endif


%package openldap
Summary:       OpenLDAP plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%description openldap
This plugin for collectd reads monitoring information
from OpenLDAP's cn=Monitor subtree.


%package -n perl-Collectd
Summary:       Perl bindings for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%description -n perl-Collectd
This package contains the Perl bindings and plugin for collectd.


%package pinba
Summary:       Pinba plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: protobuf-c-devel
%description pinba
This plugin receives profiling information from Pinba,
an extension for the PHP interpreter.


%package ping
Summary:       Ping plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: liboping-devel
%description ping
This plugin for collectd provides network latency statistics.


%package postgresql
Summary:       PostgreSQL plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: postgresql-devel
%description postgresql
PostgreSQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package redis
Summary:       Redis plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description redis
The Redis plugin connects to one or more instances of Redis, a key-value store,
and collects usage information using the hiredis library.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package rrdcached
Summary:       RRDCacheD plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdcached
This plugin uses the RRDtool accelerator daemon, rrdcached(1),
to store values to RRD files in an efficient manner.
%endif


%package rrdtool
Summary:       RRDTool plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdtool
This plugin for collectd provides rrdtool support.


%ifnarch ppc sparc sparc64
%package sensors
Summary:       Libsensors module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lm_sensors-devel
%description sensors
This plugin for collectd provides querying of sensors supported by
lm_sensors.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package smart
Summary:       SMART plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libatasmart-devel
%description smart
This plugin for collectd collects SMART statistics,
notably load cycle count, temperature and bad sectors.
%endif


%package snmp
Summary:       SNMP module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel
%description snmp
This plugin for collectd provides querying of net-snmp.


%if 0%{?fedora} || 0%{?rhel} >= 6
%ifarch %ix86 x86_64
%package turbostat
Summary:       Turbostat module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libcap-devel
%description turbostat
This plugin for collectd reads CPU frequency and C-state residency
on modern Intel turbo-capable processors.
%endif
%endif


%package varnish
Summary:       Varnish plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: varnish-libs-devel
%description varnish
This plugin collects information about Varnish, an HTTP accelerator.


%if 0%{?fedora} || 0%{?rhel} >= 6
%ifnarch ppc ppc64 sparc sparc64
%package virt
Summary:       Libvirt plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libvirt-devel
BuildRequires: libxml2-devel
%description virt
This plugin collects information from virtualized guests.
%endif
%endif


%package web
Summary:       Contrib web interface to viewing rrd files
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      collectd-rrdtool = %{version}-%{release}
Requires:      perl-HTML-Parser, perl-Regexp-Common, rrdtool-perl, httpd
%description web
This package will allow for a simple web interface to view rrd files created by
collectd.


%if 0%{?fedora} || 0%{?rhel} >= 7
%package write_redis
Summary:       Redis output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description write_redis
This plugin can send data to Redis.
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%package write_riemann
Summary:       Riemann output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: riemann-c-client-devel
%description write_riemann
This plugin can send data to Riemann.
%endif


%package write_sensu
Summary:       Sensu output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_sensu
This plugin can send data to Sensu.


%package write_tsdb
Summary:       OpenTSDB output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_tsdb
This plugin can send data to OpenTSDB.


%package zookeeper
Summary:       Zookeeper plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description zookeeper
This is a collectd plugin that reads data from Zookeeper's MNTR command.


%prep
%setup -q
%patch0 -p1

# recompile generated files
touch src/pinba.proto


%build
PATH="$PATH:/usr/pgsql-9.4/bin" \
%configure \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --without-included-ltdl \
    --enable-all-plugins \
    --disable-static \
    --disable-apple_sensors \
    --disable-aquaero \
    --disable-barometer \
    --disable-grpc \
%ifarch ppc ppc64
    --disable-virt \
%endif
    --disable-lpar \
    --disable-memcachec \
    --disable-mic \
    --disable-netapp \
%ifarch s390 s390x
    --disable-nut \
%endif
    --disable-onewire \
    --disable-oracle \
    --disable-pf \
    --disable-routeros \
%ifarch ppc sparc sparc64
    --disable-sensors \
%endif
    --disable-sigrok \
    --disable-tape \
    --disable-tokyotyrant \
%ifnarch %ix86 x86_64
    --disable-turbostat \
%endif
    --disable-write_kafka \
    --disable-write_mongodb \
    --disable-xencpu \
    --disable-xmms \
    --disable-zone \
%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
    --disable-curl_json \
    --disable-dns \
    --disable-ethstat \
    --disable-iptables \
    --disable-notify_desktop \
    --disable-python \
    --disable-turbostat \
    --disable-virt \
%endif
%if 0%{?rhel} > 0 && 0%{?rhel} <= 6
    --disable-ceph \
    --disable-cpusleep \
    --disable-gmond \
    --disable-gps \
    --disable-ipvs \
    --disable-log_logstash \
    --disable-lvm \
    --disable-modbus \
    --disable-mqtt \
    --disable-netlink \
    --disable-redis \
    --disable-rrdcached \
    --disable-smart \
    --disable-write_redis \
    --disable-write_riemann \
%endif
    --with-java=%{java_home}/ \
%if 0%{?fedora} || 0%{?rhel} >= 6
    --with-python \
%endif
    --with-perl-bindings=INSTALLDIRS=vendor \
    --disable-werror

make %{?_smp_mflags}


%install
%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
rm -rf %{buildroot}
%endif
rm -rf contrib/SpamAssassin
make install DESTDIR=%{buildroot}

%if 0%{?fedora} || 0%{?rhel} >= 7
%{__install} -Dp -m0644 contrib/systemd.collectd.service %{buildroot}%{_unitdir}/collectd.service
%else
%{__install} -Dp -m0755 contrib/redhat/init.d-collectd %{buildroot}%{_initrddir}/collectd
%endif
install -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/rrd
install -d -m0755 %{buildroot}%{_datadir}/collectd/collection3/
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d/

find contrib/ -type f -exec chmod a-x {} \;

# Remove Perl hidden .packlist files.
find %{buildroot} -name .packlist -delete
# Remove Perl temporary file perllocal.pod
find %{buildroot} -name perllocal.pod -delete

# copy web interface
cp -ad contrib/collection3/* %{buildroot}%{_datadir}/collectd/collection3/
cp -pv %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf %{buildroot}%{_sysconfdir}/collection.conf
(
cd %{buildroot}%{_datadir}/collectd/collection3/etc && \
ln -sf %{_sysconfdir}/collection.conf
)
cp -pv %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/collectd.conf
chmod +x %{buildroot}%{_datadir}/collectd/collection3/bin/*.cgi

# Move the Perl examples to a separate directory.
mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;

# Move config contribs
mkdir -p %{buildroot}%{_sysconfdir}/collectd.d/
cp %{SOURCE91} %{buildroot}%{_sysconfdir}/collectd.d/apache.conf
cp %{SOURCE92} %{buildroot}%{_sysconfdir}/collectd.d/email.conf
cp %{SOURCE93} %{buildroot}%{_sysconfdir}/collectd.d/mysql.conf
cp %{SOURCE94} %{buildroot}%{_sysconfdir}/collectd.d/nginx.conf
cp %{SOURCE95} %{buildroot}%{_sysconfdir}/collectd.d/sensors.conf
cp %{SOURCE96} %{buildroot}%{_sysconfdir}/collectd.d/snmp.conf
cp %{SOURCE97} %{buildroot}%{_sysconfdir}/collectd.d/rrdtool.conf

# configs for subpackaged plugins
mods="ipmi perl ping postgresql"
%if 0%{?fedora} || 0%{?rhel} >= 6
mods="$mods dns libvirt"
%endif
%ifnarch s390 s390x
mods="$mods nut"
%endif
for p in $mods
do
cat > %{buildroot}%{_sysconfdir}/collectd.d/$p.conf <<EOF
LoadPlugin $p
EOF
done

# *.la files shouldn't be distributed.
rm -f %{buildroot}/%{_libdir}/{collectd/,}*.la


%check
make check


%post
/sbin/ldconfig
%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_post collectd.service
%else
/sbin/chkconfig --add collectd || :
%endif


%preun
%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_preun collectd.service
%else
# stop collectd only when uninstalling
if [ $1 -eq 0 ]; then
       /sbin/service collectd stop >/dev/null 2>&1 || :
       /sbin/chkconfig --del collectd || :
fi
%endif


%postun
/sbin/ldconfig
%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_postun_with_restart collectd.service
%else
# restart collectd only when upgrading
if [ $1 -eq 1 ]; then
       /sbin/service collectd condrestart >/dev/null 2>&1 || :
fi
%endif


%files
%if 0%{?fedora} || 0%{?rhel} >= 7
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/collectd.conf
%config(noreplace) %{_sysconfdir}/collectd.d/
%exclude %{_sysconfdir}/collectd.d/apache.conf
%if 0%{?fedora} || 0%{?rhel} >= 6
%exclude %{_sysconfdir}/collectd.d/dns.conf
%endif
%exclude %{_sysconfdir}/collectd.d/email.conf
%exclude %{_sysconfdir}/collectd.d/ipmi.conf
%if 0%{?fedora} || 0%{?rhel} >= 6
%exclude %{_sysconfdir}/collectd.d/libvirt.conf
%endif
%exclude %{_sysconfdir}/collectd.d/mysql.conf
%exclude %{_sysconfdir}/collectd.d/nginx.conf
%ifnarch s390 s390x
%exclude %{_sysconfdir}/collectd.d/nut.conf
%endif
%exclude %{_sysconfdir}/collectd.d/perl.conf
%exclude %{_sysconfdir}/collectd.d/ping.conf
%exclude %{_sysconfdir}/collectd.d/postgresql.conf
%exclude %{_datadir}/collectd/postgresql_default.conf
%exclude %{_sysconfdir}/collectd.d/rrdtool.conf
%exclude %{_sysconfdir}/collectd.d/sensors.conf
%exclude %{_sysconfdir}/collectd.d/snmp.conf

%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/collectd.service
%else
%{_initrddir}/collectd
%endif
%{_bindir}/collectd-nagios
%{_bindir}/collectdctl
%{_bindir}/collectd-tg
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%dir %{_localstatedir}/lib/collectd/

%dir %{_libdir}/collectd

%{_libdir}/collectd/aggregation.so
%{_libdir}/collectd/apcups.so
%{_libdir}/collectd/battery.so
%{_libdir}/collectd/cgroups.so
%{_libdir}/collectd/conntrack.so
%{_libdir}/collectd/contextswitch.so
%{_libdir}/collectd/cpu.so
%{_libdir}/collectd/cpufreq.so
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_libdir}/collectd/cpusleep.so
%endif
%{_libdir}/collectd/csv.so
%{_libdir}/collectd/df.so
%{_libdir}/collectd/disk.so
%{_libdir}/collectd/entropy.so
%if 0%{?fedora} || 0%{?rhel} >= 6
%{_libdir}/collectd/ethstat.so
%endif
%{_libdir}/collectd/exec.so
%{_libdir}/collectd/fhcount.so
%{_libdir}/collectd/filecount.so
%{_libdir}/collectd/fscache.so
%{_libdir}/collectd/hddtemp.so
%{_libdir}/collectd/interface.so
%{_libdir}/collectd/ipc.so
%{_libdir}/collectd/irq.so
%{_libdir}/collectd/load.so
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_libdir}/collectd/log_logstash.so
%endif
%{_libdir}/collectd/logfile.so
%{_libdir}/collectd/madwifi.so
%{_libdir}/collectd/match_empty_counter.so
%{_libdir}/collectd/match_hashed.so
%{_libdir}/collectd/match_regex.so
%{_libdir}/collectd/match_timediff.so
%{_libdir}/collectd/match_value.so
%{_libdir}/collectd/mbmon.so
%{_libdir}/collectd/md.so
%{_libdir}/collectd/memcached.so
%{_libdir}/collectd/memory.so
%{_libdir}/collectd/multimeter.so
%{_libdir}/collectd/network.so
%{_libdir}/collectd/nfs.so
%{_libdir}/collectd/notify_nagios.so
%{_libdir}/collectd/ntpd.so
%{_libdir}/collectd/numa.so
%{_libdir}/collectd/olsrd.so
%{_libdir}/collectd/openvpn.so
%{_libdir}/collectd/powerdns.so
%{_libdir}/collectd/processes.so
%{_libdir}/collectd/protocols.so
%if 0%{?fedora} || 0%{?rhel} >= 6
%{_libdir}/collectd/python.so
%endif
%{_libdir}/collectd/serial.so
%{_libdir}/collectd/statsd.so
%{_libdir}/collectd/swap.so
%{_libdir}/collectd/syslog.so
%{_libdir}/collectd/table.so
%{_libdir}/collectd/tail.so
%{_libdir}/collectd/tail_csv.so
%{_libdir}/collectd/target_notification.so
%{_libdir}/collectd/target_replace.so
%{_libdir}/collectd/target_scale.so
%{_libdir}/collectd/target_set.so
%{_libdir}/collectd/target_v5upgrade.so
%{_libdir}/collectd/tcpconns.so
%{_libdir}/collectd/teamspeak2.so
%{_libdir}/collectd/ted.so
%{_libdir}/collectd/thermal.so
%{_libdir}/collectd/threshold.so
%{_libdir}/collectd/unixsock.so
%{_libdir}/collectd/uptime.so
%{_libdir}/collectd/users.so
%{_libdir}/collectd/uuid.so
%{_libdir}/collectd/vmem.so
%{_libdir}/collectd/vserver.so
%{_libdir}/collectd/wireless.so
%{_libdir}/collectd/write_graphite.so
%{_libdir}/collectd/write_http.so
%{_libdir}/collectd/write_log.so
%{_libdir}/collectd/zfs_arc.so

%{_datadir}/collectd/types.db

# collectdclient - TBD reintroduce -devel subpackage?
%{_libdir}/libcollectdclient.so
%{_libdir}/libcollectdclient.so.1
%{_libdir}/libcollectdclient.so.1.0.0
%{_libdir}/pkgconfig/libcollectdclient.pc
%{_includedir}/collectd/client.h
%{_includedir}/collectd/lcc_features.h
%{_includedir}/collectd/network.h
%{_includedir}/collectd/network_buffer.h

%doc %{_mandir}/man1/collectd.1*
%doc %{_mandir}/man1/collectdctl.1*
%doc %{_mandir}/man1/collectd-nagios.1*
%doc %{_mandir}/man1/collectd-tg.1*
%doc %{_mandir}/man1/collectdmon.1*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-exec.5*
%if 0%{?fedora} || 0%{?rhel} >= 6
%doc %{_mandir}/man5/collectd-python.5*
%else
%exclude %{_mandir}/man5/collectd-python.5*
%endif
%doc %{_mandir}/man5/collectd-threshold.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%doc %{_mandir}/man5/types.db.5*

%files amqp
%{_libdir}/collectd/amqp.so


%files apache
%{_libdir}/collectd/apache.so
%config(noreplace) %{_sysconfdir}/collectd.d/apache.conf


%files ascent
%{_libdir}/collectd/ascent.so


%files bind
%{_libdir}/collectd/bind.so


%if 0%{?fedora} || 0%{?rhel} >= 7
%files ceph
%{_libdir}/collectd/ceph.so
%endif


%files chrony
%{_libdir}/collectd/chrony.so


%files curl
%{_libdir}/collectd/curl.so


%if 0%{?fedora} || 0%{?rhel} >= 6
%files curl_json
%{_libdir}/collectd/curl_json.so
%endif


%files curl_xml
%{_libdir}/collectd/curl_xml.so


%files dbi
%{_libdir}/collectd/dbi.so


%if 0%{?fedora} || 0%{?rhel} >= 6
%files dns
%{_libdir}/collectd/dns.so
%config(noreplace) %{_sysconfdir}/collectd.d/dns.conf
%endif


%files drbd
%{_libdir}/collectd/drbd.so


%files email
%{_libdir}/collectd/email.so
%config(noreplace) %{_sysconfdir}/collectd.d/email.conf
%doc %{_mandir}/man5/collectd-email.5*


%files generic-jmx
%{_datadir}/collectd/java/generic-jmx.jar


%if 0%{?fedora} || 0%{?rhel} >= 7
%files gmond
%{_libdir}/collectd/gmond.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files gps
%{_libdir}/collectd/gps.so
%endif


%files ipmi
%{_libdir}/collectd/ipmi.so
%config(noreplace) %{_sysconfdir}/collectd.d/ipmi.conf


%if 0%{?fedora} || 0%{?rhel} >= 6
%files iptables
%{_libdir}/collectd/iptables.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files ipvs
%{_libdir}/collectd/ipvs.so
%endif


%files java
%{_libdir}/collectd/java.so
%dir %{_datadir}/collectd/java/
%{_datadir}/collectd/java/collectd-api.jar
%doc %{_mandir}/man5/collectd-java.5*


%files lua
%{_mandir}/man5/collectd-lua*
%{_libdir}/collectd/lua.so


%if 0%{?fedora} || 0%{?rhel} >= 7
%files lvm
%{_libdir}/collectd/lvm.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files modbus
%{_libdir}/collectd/modbus.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files mqtt
%{_libdir}/collectd/mqtt.so
%endif


%files mysql
%{_libdir}/collectd/mysql.so
%config(noreplace) %{_sysconfdir}/collectd.d/mysql.conf


%if 0%{?fedora} || 0%{?rhel} >= 7
%files netlink
%{_libdir}/collectd/netlink.so
%endif


%files nginx
%{_libdir}/collectd/nginx.so
%config(noreplace) %{_sysconfdir}/collectd.d/nginx.conf


%if 0%{?fedora} || 0%{?rhel} >= 6
%files notify_desktop
%{_libdir}/collectd/notify_desktop.so
%endif


%files notify_email
%{_libdir}/collectd/notify_email.so


%ifnarch s390 s390x
%files nut
%{_libdir}/collectd/nut.so
%config(noreplace) %{_sysconfdir}/collectd.d/nut.conf
%endif


%files openldap
%{_libdir}/collectd/openldap.so


%files -n perl-Collectd
%doc perl-examples/*
%{_libdir}/collectd/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%config(noreplace) %{_sysconfdir}/collectd.d/perl.conf
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*


%files pinba
%{_libdir}/collectd/pinba.so


%files ping
%{_libdir}/collectd/ping.so
%config(noreplace) %{_sysconfdir}/collectd.d/ping.conf


%files postgresql
%{_libdir}/collectd/postgresql.so
%config(noreplace) %{_sysconfdir}/collectd.d/postgresql.conf
%{_datadir}/collectd/postgresql_default.conf


%if 0%{?fedora} || 0%{?rhel} >= 7
%files redis
%{_libdir}/collectd/redis.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files rrdcached
%{_libdir}/collectd/rrdcached.so
%endif


%files rrdtool
%{_libdir}/collectd/rrdtool.so
%config(noreplace) %{_sysconfdir}/collectd.d/rrdtool.conf


%ifnarch ppc sparc sparc64
%files sensors
%{_libdir}/collectd/sensors.so
%config(noreplace) %{_sysconfdir}/collectd.d/sensors.conf
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files smart
%{_libdir}/collectd/smart.so
%endif


%files snmp
%{_libdir}/collectd/snmp.so
%config(noreplace) %{_sysconfdir}/collectd.d/snmp.conf
%doc %{_mandir}/man5/collectd-snmp.5*


%if 0%{?fedora} || 0%{?rhel} >= 6
%ifarch %ix86 x86_64
%files turbostat
%{_libdir}/collectd/turbostat.so
%endif
%endif


%files varnish
%{_libdir}/collectd/varnish.so


%if 0%{?fedora} || 0%{?rhel} >= 6
%ifnarch ppc ppc64 sparc sparc64
%files virt
%{_libdir}/collectd/virt.so
%config(noreplace) %{_sysconfdir}/collectd.d/libvirt.conf
%endif
%endif


%files web
%{_datadir}/collectd/collection3/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/collectd.conf
%config(noreplace) %{_sysconfdir}/collection.conf


%if 0%{?fedora} || 0%{?rhel} >= 7
%files write_redis
%{_libdir}/collectd/write_redis.so
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%files write_riemann
%{_libdir}/collectd/write_riemann.so
%endif


%files write_sensu
%{_libdir}/collectd/write_sensu.so


%files write_tsdb
%{_libdir}/collectd/write_tsdb.so


%files zookeeper
%{_libdir}/collectd/zookeeper.so


%changelog
* Wed Dec  7 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 5.6.2-0.3
- fix RHEL-5 RHEL-6

* Wed Dec  7 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 5.6.2-0.2
- support Fedora 25/26 and RHEL-5 and RHEL-6

* Thu Sep 15 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.6.0-1
- Upstream released new version: https://collectd.org/news.shtml#news99
- Enable new plugins: chrony, cpusleep, gps, lua, mqtt, zfs_arc

* Tue Jul 26 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.2-1
- Upstream released new version (https://collectd.org/news.shtml#news98)
- Contains fix for CVE-2016-6254
- Drop a few patches applied upstream
- Use Type=notify in systemd unit now that collectd support it.
- Enable zfs_arc plugin (#1359669)

* Wed Mar 16 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.1-3
- Enable modbus plugin (#1310854)

* Fri Feb 05 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.1-2
- Fix build on ppc64

* Fri Feb 05 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.1-1
- Upstream released new version

* Sun Dec 06 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-3
- Fix regression in swap plugin (#1261237)

* Mon Jun 22 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-2
- Fix 404 while loading stylesheet in collection3

* Mon Jun 22 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-1
- Upstream released new version
- New plugins for Ceph, DRBD, SMART, turbostat, Redis and more

* Fri Feb 27 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.2-1
- Upstream released new version
- Enable write_riemann plugin
- Use collection.conf from upstream
- Improve the systemd unit a bit

* Tue Jan 28 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-1
- Upstream released new version: http://collectd.org/news.shtml#news95

* Mon Dec 23 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.3.1-1
- Upstream released new version
- Enable memcached plugin (#1036422)
- Stop running autoreconf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.3.0-4
- Perl 5.18 rebuild

* Mon Jun 03 2013 Kevin Fenzi <kevin@scrye.com> 5.3.0-3
- Rebuild for new ganglia

* Mon May 27 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.3.0-2
- BuildRequire static version of iproute (#967214)

* Sat Apr 27 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.3.0-1
- update to 5.3.0
  http://mailman.verplant.org/pipermail/collectd/2013-April/005749.html
- enable all plugins we can enable
- filter plugins from Provides
- use new systemd macros (#850062)
- modernize specfile

* Mon Apr 22 2013 Alan Pevec <apevec@redhat.com> 5.2.2-1
- update to 5.2.2
  http://mailman.verplant.org/pipermail/collectd/2013-April/005749.html
- build with PIE flags rhbz#954322

* Mon Feb 04 2013 Alan Pevec <apevec@redhat.com> 5.2.1-1
- update to 5.2.1
  http://mailman.verplant.org/pipermail/collectd/2013-January/005577.html

* Mon Nov 26 2012 Alan Pevec <apevec@redhat.com> 5.2.0-1
- update to 5.2.0 from Steve Traylen rhbz#877721

* Wed Nov 21 2012 Alan Pevec <apevec@redhat.com> 5.1.1-1
- update to 5.1.1
- spec cleanups from Ruben Kerkhof
- fix postgresql_default.conf location rhbz#681615
- fix broken configuration for httpd 2.4 rhbz#871385

* Mon Nov 19 2012 Alan Pevec <apevec@redhat.com> 5.0.5-1
- new upstream version 5.0.5
  http://mailman.verplant.org/pipermail/collectd/2012-November/005465.html

* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> 5.0.4-1
- New upstream release, version bump to 5 (#743894) from Andrew Elwell

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 4.10.7-2
- Perl 5.16 rebuild

* Tue Apr 03 2012 Alan Pevec <apevec@redhat.com> 4.10.7-1
- new upstream release 4.10.7
  http://mailman.verplant.org/pipermail/collectd/2012-April/005045.html

* Wed Feb 29 2012 Alan Pevec <apevec@redhat.com> 4.10.6-1
- new upstream release 4.10.6
  http://mailman.verplant.org/pipermail/collectd/2012-February/004932.html

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Alan Pevec <apevec@redhat.com> 4.10.4-1
- new upstream version 4.10.4
  http://mailman.verplant.org/pipermail/collectd/2011-October/004777.html
- collectd-web config file DataDir value wrong rhbz#719809
- Python plugin doesn't work rhbz#739593
- Add systemd service file. (thanks Paul P. Komkoff Jr) rhbz#754460

* Fri Jul 29 2011 Kevin Fenzi <kevin@scrye.com> - 4.10.3-8
- Rebuild for new snmp again.

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 4.10.3-7
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.10.3-6
- Perl mass rebuild

* Fri Jul 08 2011 Kevin Fenzi <kevin@scrye.com> - 4.10.3-5
- Rebuild for new snmp

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.10.3-4
- Perl mass rebuild

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 4.10.3-3
- fix build on s390(x)

* Tue Apr 19 2011 Alan Pevec <apevec@redhat.com> 4.10.3-2
- re-enable nut plugin rhbz#465729 rhbz#691380

* Tue Mar 29 2011 Alan Pevec <apevec@redhat.com> 4.10.3-1
- new upstream version 4.10.3
  http://collectd.org/news.shtml#news87
- disable nut 2.6 which fails collectd check:
  libupsclient  . . . . no (symbol upscli_connect not found)

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 4.10.2-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Dan Horák <dan[at]danny.cz> 4.10.2-2
- no nut on s390(x)

* Thu Dec 16 2010 Alan Pevec <apevec@redhat.com> 4.10.2-1
- New upstream version 4.10.2
- http://collectd.org/news.shtml#news86
- explicitly disable/enable all plugins, fixes FTBFS bz#660936

* Thu Nov 04 2010 Alan Pevec <apevec@redhat.com> 4.10.1-1
- New upstream version 4.10.1
  http://collectd.org/news.shtml#news85

* Sat Oct 30 2010 Richard W.M. Jones <rjones@redhat.com> 4.10.0-3
- Bump and rebuild for updated libnetsnmp.so.

* Wed Sep 29 2010 jkeating - 4.10.0-2
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Robert Scheck <robert@fedoraproject.org> 4.10.0-1
- New upstream version 4.10.0 (thanks to Mike McGrath)

* Tue Jun 08 2010 Alan Pevec <apevec@redhat.com> 4.9.2-1
- New upstream version 4.9.2
  http://collectd.org/news.shtml#news83

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.9.1-3
- Mass rebuild with perl-5.12.0

* Fri Mar 26 2010 Alan Pevec <apevec@redhat.com> 4.9.1-2
- enable ping plugin bz#541744

* Mon Mar 08 2010 Lubomir Rintel <lkundrak@v3.sl> 4.9.1-1
- New upstream version 4.9.1
  http://collectd.org/news.shtml#news81

* Tue Feb 16 2010 Alan Pevec <apevec@redhat.com> 4.8.3-1
- New upstream version 4.8.3
  http://collectd.org/news.shtml#news81
- FTBFS bz#564943 - system libiptc is not usable and owniptc fails to compile:
  add a patch from upstream iptables.git to fix owniptc compilation

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 4.8.1-3
- rebuild against perl 5.10.1

* Fri Nov 27 2009 Alan Pevec <apevec@redhat.com> 4.8.1-2
- use Fedora libiptc, owniptc in collectd sources fails to compile

* Wed Nov 25 2009 Alan Pevec <apevec@redhat.com> 4.8.1-1
- update to 4.8.1 (Florian La Roche) bz# 516276
- disable ping plugin until liboping is packaged bz# 541744

* Fri Sep 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.6.5-1
- update to 4.6.5
- disable ppc/ppc64 due to compile error

* Wed Sep 02 2009 Alan Pevec <apevec@redhat.com> 4.6.4-1
- fix condrestart: on upgrade collectd is not restarted, bz# 516273
- collectd does not re-connect to libvirtd, bz# 480997
- fix unpackaged files https://bugzilla.redhat.com/show_bug.cgi?id=516276#c4
- New upstream version 4.6.4
  http://collectd.org/news.shtml#news69

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.6.2-5
- rebuilt with new openssl

* Thu Aug  6 2009 Richard W.M. Jones <rjones@redhat.com> - 4.6.2-4
- Force rebuild to test FTBFS issue.
- lib/collectd/types.db seems to have moved to share/collectd/types.db

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Alan Pevec <apevec@redhat.com> 4.6.2-1
- New upstream version 4.6.2
  http://collectd.org/news.shtml#news64

* Tue Mar 03 2009 Alan Pevec <apevec@redhat.com> 4.5.3-2
- patch for strict-aliasing issue in liboping.c

* Mon Mar 02 2009 Alan Pevec <apevec@redhat.com> 4.5.3-1
- New upstream version 4.5.3
- fixes collectd is built without iptables plugin, bz# 479208
- list all expected plugins explicitly to avoid such bugs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 4.5.1-3
- Rebuild against new mysql client.

* Sun Dec 07 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2.1
- fix subpackages, bz# 475093

* Sun Nov 30 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2
- workaround for https://bugzilla.redhat.com/show_bug.cgi?id=468067

* Wed Oct 22 2008 Alan Pevec <apevec@redhat.com> 4.5.1-1
- New upstream version 4.5.1, bz# 470943
  http://collectd.org/news.shtml#news59
- enable Network UPS Tools (nut) plugin, bz# 465729
- enable postgresql plugin
- spec cleanup, bz# 473641

* Fri Aug 01 2008 Alan Pevec <apevec@redhat.com> 4.4.2-1
- New upstream version 4.4.2.

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-4
- Fix a typo introduced by previous change that prevented building in el5

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-3
- Make this compile with older perl package
- Turn dependencies on packages to dependencies on Perl modules
- Add default attributes for files

* Thu Jun 12 2008 Alan Pevec <apevec@redhat.com> 4.4.1-2
- Split rrdtool into a subpackage (Chris Lalancette)
- cleanup subpackages, split dns plugin, enable ipmi
- include /etc/collectd.d (bz#443942)

* Mon Jun 09 2008 Alan Pevec <apevec@redhat.com> 4.4.1-1
- New upstream version 4.4.1.
- plugin changes: reenable iptables, disable ascent

* Tue May 27 2008 Alan Pevec <apevec@redhat.com> 4.4.0-2
- disable iptables/libiptc

* Mon May 26 2008 Alan Pevec <apevec@redhat.com> 4.4.0-1
- New upstream version 4.4.0.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-9
- Added {?dist} to release number (thanks Alan Pevec).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-8
- Bump release number so we can tag this in Rawhide.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-6
- Exclude perl.so from the main package.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-5
- Put the perl bindings and plugin into a separate perl-Collectd
  package.  Note AFAICT from the manpage, the plugin and Collectd::*
  perl modules must all be packaged together.

* Wed Apr 16 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-4
- Remove -devel subpackage.
- Add subpackages for apache, email, mysql, nginx, sensors,
  snmp (thanks Richard Shade).
- Add subpackages for perl, libvirt.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-2
- Install Perl bindings in vendor dir not site dir.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-1
- New upstream version 4.3.2.
- Create a -devel subpackage for development stuff, examples, etc.
- Use .bz2 package instead of .gz.
- Remove fix-hostname patch, now upstream.
- Don't mark collectd init script as config.
- Enable MySQL, sensors, email, apache, Perl, unixsock support.
- Don't remove example Perl scripts.
- Package types.db(5) manpage.
- Fix defattr.
- Build in koji to find the full build-requires list.

* Mon Apr 14 2008 Richard W.M. Jones <rjones@redhat.com> - 4.2.3.100.g79b0797-2
- Prepare for Fedora package review:
- Clarify license is GPLv2 (only).
- Setup should be quiet.
- Spelling mistake in original description fixed.
- Don't include NEWS in doc - it's an empty file.
- Convert some other doc files to UTF-8.
- config(noreplace) on init file.

* Thu Jan 10 2008 Chris Lalancette <clalance@redhat.com> - 4.2.3.100.g79b0797.1.ovirt
- Update to git version 79b0797
- Remove *.pm files so we don't get a bogus dependency
- Re-enable rrdtool; we will need it on the WUI side anyway

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 4.2.0-1 - 5946+/dag
- Updated to release 4.2.0.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 3.11.5-1
- Initial package. (using DAR)
