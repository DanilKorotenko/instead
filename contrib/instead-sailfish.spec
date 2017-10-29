Summary:	simple text adventures/visual novels engine and game
Name:		instead
Version:	3.1.2
Release:	1%{?dist}
License:	MIT
URL:		http://instead.sourceforge.net
Source0:	%{name}_%{version}.tar.gz
Group:		Amusements/Games
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: SDL2-devel, SDL2_mixer-devel, SDL2_image-devel, SDL2_ttf-devel, lua-devel, libaudioresource-devel, glib2-devel

%description
Simple text adventures/visual novels engine and game
Visual novell/text quest-like game in Russian with engine.

%prep
%setup -q

echo -e "2\n\/usr" | ./configure.sh
cat >>config.make <<EOF
CFLAGS+=\$(shell pkg-config --cflags glib-2.0) \$(shell pkg-config --cflags audioresource) -DSAILFISHOS=1
LDFLAGS+=\$(shell pkg-config --libs glib-2.0) \$(shell pkg-config --libs audioresource)
EOF
%build
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT ICONPATH=/usr/share/icons/hicolor/128x128/apps/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/doc/*
%{_mandir}/*