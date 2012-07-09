%define debug_package %{nil}

Summary:	Nagios plugin - check_mongodb
Name:		nagios-plugins-mongodb
Version:	20120709git
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		https://github.com/mzupan/nagios-plugin-mongodb
Source0:	check_mongodb
Source1:	README.md
Requires:	nagios-plugins, pymongo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A plugin for nagios that will check mongodb. Requires pymongo.

%prep
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" check_crond

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 check_mongodb %{buildroot}%{_libdir}/nagios/plugins/check_mongodb

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/nagios/plugins/check_crond

%changelog
* Mon Jul 09 2012  Ilya A. Otyutskiy <sharp@thesharp.ru> - 20120709git-1.vortex
- Initial packaging.

