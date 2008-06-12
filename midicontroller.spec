%define name	midicontroller
%define version	041011
%define release %mkrel 3

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
perl -p -i -e "s|-g -O2|$RPM_OPT_FLAGS||g" Makefile

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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

