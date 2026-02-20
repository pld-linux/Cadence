Summary:	Set of tools useful for audio production
Name:		Cadence
Version:	0.9.0
Release:	3
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/falkTX/Cadence/archive/v0.9.0/%{name}-%{version}.tar.gz
# Source0-md5:	3031db18be95c62a758c2793498549a7
Patch0:		libdir.patch
Patch1:		kernel_check.patch
URL:		http://kxstudio.linuxaudio.org/Applications:Cadence
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	python-PyQt5-devel-tools
BuildRequires:	python3-PyQt5
BuildRequires:	python3-PyQt5-uic
BuildRequires:	qt5-build
BuildRequires:	rpm-pythonprov
Requires:	python3-PyQt5
Requires:	python3-dbus
Suggests:	a2jmidid
Suggests:	jack-capture
Suggests:	pulseaudio-jack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cadence is a set of tools useful for audio production.

- Cadence - The main app. It performs system checks, manages JACK,
  calls other tools and make system tweaks.

- Cadence-JackMeter - Digital peak meter for JACK.

- Cadence-JackSettings - Simple and easy-to-use configure dialog for
  jackdbus.

- Cadence-Logs - Small tool that shows JACK, A2J, LASH and LADISH logs
  in a multi-tab window.

- Cadence-Render - Tool to record (or 'render') a JACK project using
  jack-capture, controlled by JACK Transport.

- Cadence-XY Controller - Simple XY widget that sends and receives
  data from Jack MIDI.

- Catarina - A Patchbay test app.

- Catia - JACK Patchbay, with some neat features like A2J bridge
  support and JACK Transport.

- Claudia - LADISH frontend; just like Catia, but focused at session
  management through LADISH.

- Claudia-Launcher - A multimedia application launcher with LADISH
  support.

%prep
%setup -q

%patch -P0 -p1
%patch -P1 -p1
sed -i -e 's@^LIBDIR = .*@LIBDIR = "%{_libdir}"@' src/shared_cadence.py

%build
%{__make} \
	PYUIC=pyuic5-3 \
	PYRCC=pyrcc5 \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -i -e '1s,^#!.*python3\?,#!%{__python3},' \
	$RPM_BUILD_ROOT/%{_bindir}/* \
	$RPM_BUILD_ROOT/%{_datadir}/cadence/src/*

%py3_comp $RPM_BUILD_ROOT%{_datadir}/cadence

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md TODO
%attr(755,root,root) %{_bindir}/cadence
%attr(755,root,root) %{_bindir}/cadence-aloop-daemon
%attr(755,root,root) %{_bindir}/cadence-jackmeter
%attr(755,root,root) %{_bindir}/cadence-jacksettings
%attr(755,root,root) %{_bindir}/cadence-logs
%attr(755,root,root) %{_bindir}/cadence-pulse2jack
%attr(755,root,root) %{_bindir}/cadence-pulse2loopback
%attr(755,root,root) %{_bindir}/cadence-render
%attr(755,root,root) %{_bindir}/cadence-session-start
%attr(755,root,root) %{_bindir}/cadence-xycontroller
%attr(755,root,root) %{_bindir}/catarina
%attr(755,root,root) %{_bindir}/catia
%attr(755,root,root) %{_bindir}/claudia
%attr(755,root,root) %{_bindir}/claudia-launcher
%{_datadir}/cadence
%{_iconsdir}/hicolor/*/apps/*
%{_desktopdir}/cadence.desktop
%{_desktopdir}/catarina.desktop
%{_desktopdir}/catia.desktop
%{_desktopdir}/claudia.desktop
%{_desktopdir}/claudia-launcher.desktop
/etc/xdg/autostart/cadence-session-start.desktop
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/*
