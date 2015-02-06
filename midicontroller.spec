%define name	midicontroller
%define version	041011
%define release 6

Name: 	 	%{name}
Summary:	Graphical sliders to send MIDI control commands	
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/midicontrol/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig libalsa-devel libglademm2.4-devel

%description
This is a small program that lets you set MIDI controller values using sliders
and buttons in a GTK+ window. The GUI is an XML-based Glade file which can be
replaced without rebuilding the program, so you can build your own controller
GUIs in Glade.

%prep
%setup -q
perl -p -i -e "s|-g -O2|$RPM_OPT_FLAGS -Wno-long-long||g" Makefile

%build
%make PREFIX=%{_prefix}
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=$RPM_BUILD_ROOT/%_prefix

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=MIDI Controller
Comment=MIDI CC Sliders
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Midi;
Encoding=UTF-8
EOF
rm -fr $RPM_BUILD_ROOT%_defaultdocdir/%name-%version

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 041011-5mdv2010.0
+ Revision: 430027
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 041011-4mdv2009.0
+ Revision: 222651
- fix 'Installed (but unpackaged) file(s) found' error
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- import midicontroller

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 041011-3mdv2007.0
- xdg menu
- %%mkrel
- fix buildrequires

* Sat Jan 15 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 041011-2mdk
- use prefix which fix location of controller.glade file
- update buildrequires

* Sun Oct 17 2004 Austin Acton <austin@mandrake.org> 041011-1mdk
- initial package

