%define	name	dsh
%define	version	0.25.7

Summary:	Distributed shell. Runs command through rsh or ssh on a cluster of machines.
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Networking/Remote access
Url:		http://www.netfort.gr.jp/~dancer/software/downloads/#dsh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	libdshconfig-devel

%description
Distributed shell. Runs command through rsh or ssh on a cluster of machines.
Requires libdshconfig to be already installed on the system

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
#%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/dsh.conf
%{_bindir}/%name
%{_mandir}/man1/dsh.1*
%{_mandir}/man5/dsh.conf.5*
%{_mandir}/ja

