Name:           pwauth
Version:        2.3.10
Release:        2%{?dist}
Summary:        External plugin for mod_authnz_external authenticator

Group:          Applications/System
License:        BSD
URL:            http://code.google.com/p/pwauth/
Source0:        http://pwauth.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        pwauth.pam
Patch1:         pwauth-strchr.patch

BuildRequires:  pam-devel
Requires(pre):  httpd

%description
Pwauth is an authenticator designed to be used with mod_auth_external
or mod_authnz_external and the Apache HTTP daemon to support reasonably
secure web authentication out of the system password database on most
versions of Unix.


%prep
%setup -q

%patch1 -p1 -b .strchr

%build
sed -i.orig -r \
    -e 's@^#define SHADOW_@/* &@' \
    -e 's@^/\* (#define PAM[^_])@\1@' \
    -e 's@^(#define (NOLOGIN_FILE|MIN_NOLOGIN_UID|SERVER_UIDS))@/* \1@' \
    config.h

sed -i.orig -r \
    -e 's@^# (LIB=-lpam -ldl)@\1@' \
    -e 's@^CFLAGS= \$\(LOCALFLAGS\)@# &@' \
    Makefile

make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS} -Wno-comment"


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/pam.d

install -p -m 4750 -t %{buildroot}%{_bindir} pwauth
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/pwauth


%clean


%files
%attr(4750,root,apache) %{_bindir}/pwauth
%attr(644,-,-) %{_sysconfdir}/pam.d/pwauth
%doc CHANGES INSTALL README


%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 05 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-1
- Initial checkin after Fedora packaging review.

* Tue Apr 17 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-0
- Initial RPM packaging.
