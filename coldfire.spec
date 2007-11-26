Name: coldfire
Version: 0.2.2
Release: %mkrel 2
Summary: A Freescale Coldfire 5206 Emulator
URL: http://www.slicer.ca/coldfire/
Source: http://www.slicer.ca/coldfire/files/coldfire-%{version}.tar.gz
Patch0: coldfire-0.2.2-gcc4.patch.bz2
Patch1: coldfire-0.2.2-manpage.patch.bz2
Group: Emulators
License: GPL
BuildRequires: libreadline-devel
BuildRequires: libncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Coldfire is a Freescale Coldfire 5206 Emulator. It currently features
all but 5 assembly instructions, a full dBug with extra functionality,
both serial ports, the parallel port, interrupts (through telnet
sessions), full exception handling, timers and timer interrupts, and
full tracing capability.

%prep
%setup -q
%patch0 -p1 -b .gcc4
%patch1 -p1 -b .manpage

%build
%configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/coldfire

install -s -m 755 coldfire %{buildroot}%{_bindir}/coldfire
install -m 644 coldfire.1 %{buildroot}%{_mandir}/man1/coldfire.1
install -m 644 boards/* %{buildroot}%{_datadir}/coldfire/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS LICENSE
%{_bindir}/coldfire
%{_mandir}/man1/coldfire.1*
%{_datadir}/coldfire/*

