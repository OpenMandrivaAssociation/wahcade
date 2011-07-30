Name:			wahcade
Version:		0.99
%define beta		pre8
Release:		%mkrel 0.%{beta}

Summary:	Front end for SDLMAME
License:	GPLv2+
Group:		Emulators
URL:		http://www.anti-particle.com/wahcade.shtml
Source0:	http://www.anti-particle.com/projects/%{name}/%{name}-%{version}%{beta}.tar.gz
Patch0:		wahcade-0.99pre8-install-fixes.patch

BuildRequires:	python

Requires:	pygtk2.0-libglade
Requires:	python-chardet
Suggests:	python-imaging
suggests:	gstreamer0.10-python
Suggests:	pygame
#Do not require stuff from Non-free
Suggests:	sdlmame-extra-data
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Wah!Cade is a GNU/Linux friendly clone of Minwah's excellent MameWAH.

It's a front end for games and emulators (e.g. the MAME arcade game emulator), 
and has been designed with arcade cabinet controls and projects in mind.

It is compatible with MameWah's config files and layouts.

It features :
 - a keyboard controlled GUI, perfect for those arcade controls,
 - a history viewer,
 - a control panel viewer,
 - a layout editor,
 - a setup editor.

%prep
%setup -q -n %{name}
%patch0 -p1 

%build
#python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

rm -f %{buildroot}%{py_platsitedir}/%{name}-%{version}*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus

%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

