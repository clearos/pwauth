%global _hardened_build 1

Name:           pwauth
Version:        2.3.10
Release:        9%{?dist}
Summary:        External plugin for mod_authnz_external authenticator

Group:          Applications/System
License:        BSD
URL:            http://code.google.com/p/pwauth/
Source0:        http://pwauth.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        pwauth.pam
Patch1:		pwauth-make.patch
Patch2:         pwauth-strchr.patch
Patch3:         pwauth-cleanup.patch

BuildRequires:  pam-devel
Requires(pre):  httpd, perl

%description
Pwauth is an authenticator designed to be used with mod_auth_external
or mod_authnz_external and the Apache HTTP daemon to support reasonably
secure web authentication out of the system password database on most
versions of Unix.


%prep
%setup -q

%patch1 -p1 -b .make
%patch2 -p1 -b .strchr
%patch3 -p1 -b .cleanup

%build
export CFLAGS="${RPM_OPT_FLAGS}"
export LDFLAGS="${RPM_LD_FLAGS}"

make %{?_smp_mflags} CFLAGS="${CFLAGS} -Wno-comment" LDFLAGS="${LDFLAGS}"


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/pam.d

install -p -m 4750 -t %{buildroot}%{_bindir} pwauth
install -p -m 0750 -t %{buildroot}%{_bindir} unixgroup
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/pwauth
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/unixgroup


%clean


%files
%defattr(-,root,root,-)
%attr(4750,-,apache) %{_bindir}/pwauth
%attr(4750,-,apache) %{_bindir}/unixgroup
%attr(644,-,-) %{_sysconfdir}/pam.d/pwauth
%attr(644,-,-) %{_sysconfdir}/pam.d/unixgroup
%doc CHANGES INSTALL README FORM_AUTH


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-5
- Fix for bz#965461
- Get rid of some of the more worrisome compiler warnings.
- Use patch instead of sed to modify Makefile.

* Fri Mar 22 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-4
- Fix for bz#924881

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 05 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-1
- Initial checkin after Fedora packaging review.

* Tue Apr 17 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-0
- Initial RPM packaging.
