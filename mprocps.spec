# $Revision: 1.2 $Date: 2000-10-10 08:49:44 $
%define 	mprocps_version	1.01-1.2.9
%define		package_version	1.01_1.2.9

Summary: 	Multicomputer process monitoring utilities
Name:		mprocps
Version:	%{package_version}
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.cs.huji.ac.il/users/mosix/contrib/mproc-%{mprocps_version}.tar.gz
Patch:		%{name}-make.patch
ExclusiveArch:	%{ix86}
Requires:	mosix-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package of utilities which report on the state of the system,
including the states of running processes, amount of memory available,
and currently-logged-in users on a Mosix multicomputer system.

%package X11
Group: X11/Utilities
Summary: X-based process monitoring utilities

%description X11
A package of X-based utilities which report on the state of the system.
These utilities generally provide graphical presentations of information
available from tools in the procps suite.

%prep
%setup -q -n mproc-1.0.1-1.2.9
%patch -p1

%build
PATH=/usr/X11R6/bin:$PATH
make CC="gcc $RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

# Since this is specific to Red Hat now, we'll leave this in the spec file.
# If others decide they like wmconfig, we'll move it to the install phase
# of the Makefile.
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install mtop.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/mtop

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

if [ -f /proc/uptime ] ; then
  /bin/mps </dev/null >/dev/null 2>&1
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) /bin/mps
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) %{_mandir}/man1/msnice.1

%config(missingok) /etc/X11/wmconfig/mtop
%doc NEWS BUGS TODO
%{_mandir}/man1/mps.1
%{_mandir}/man1/mtop.1
%{_mandir}/man1/mskill.1

%files X11
%attr(4755,root,root) /usr/X11R6/bin/XConsole
