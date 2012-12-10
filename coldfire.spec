Name:		coldfire
Version:	0.3.1
Release:	8
Summary:	A Freescale Coldfire 5206 Emulator
Group:		Emulators
License:	GPLv2
URL:		http://www.slicer.ca/coldfire/
Source:		http://www.slicer.ca/coldfire/files/coldfire-%{version}.tar.gz
Patch0:		coldfire-0.3.1-headers.patch
Patch1:		coldfire-0.2.2-manpage.patch
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)

%description
Coldfire is a Freescale Coldfire 5206 Emulator. It currently features
all but 5 assembly instructions, a full dBug with extra functionality,
both serial ports, the parallel port, interrupts (through telnet
sessions), full exception handling, timers and timer interrupts, and
full tracing capability.

%prep
%setup -q
%patch0 -p1 -b .headers
%patch1 -p1 -b .manpage

%build
%configure2_5x
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/coldfire
install -m 755 coldfire %{buildroot}%{_bindir}/coldfire
install -m 644 coldfire.1 %{buildroot}%{_mandir}/man1/coldfire.1
install -m 644 boards/* %{buildroot}%{_datadir}/coldfire/

%files
%doc README LICENSE
%{_bindir}/coldfire
%{_mandir}/man1/coldfire.1*
%{_datadir}/coldfire/*

