# $Revision: 1.5 $Date: 2001-09-19 22:35:23 $

Summary:	Multicomputer process monitoring utilities
Summary(pl):	Narzêdzia do monitorowania procesów w ¶rodowisku MOSIX
Name:		mprocps
Version:	1.01_1.2.9
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.cs.huji.ac.il/users/mosix/contrib/mproc-%{version}.tar.gz
Patch0:		%{name}-make.patch
ExclusiveArch:	%{ix86}
Requires:	mosix-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin

%description
A package of utilities which report on the state of the system,
including the states of running processes, amount of memory available,
and currently-logged-in users on a Mosix multicomputer system.

%package X11
Summary:	X-based process monitoring utilities
Summary(pl):	Narzêdzia pod X Window do monitorowania procesów MOSIX
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description X11
A package of X-based utilities which report on the state of the
system. These utilities generally provide graphical presentations of
information available from tools in the procps suite.

%prep
%setup -q -n mproc-1.0.1-1.2.9
%patch -p1

%build
PATH=%{_xbindir}:$PATH
%{__make} CC="%{__cc} %{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

# Since this is specific to Red Hat now, we'll leave this in the spec file.
# If others decide they like wmconfig, we'll move it to the install phase
# of the Makefile.
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig
install mtop.wmconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/mtop

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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/msnice.1

%config(missingok) %{_sysconfdir}/X11/wmconfig/mtop
%doc NEWS BUGS TODO
%{_mandir}/man1/mps.1*
%{_mandir}/man1/mtop.1*
%{_mandir}/man1/mskill.1*

%files X11
%defattr(644,root,root,755)
%attr(4755,root,root) %{_xbindir}/XConsole
