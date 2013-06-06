%define	majver	112
%define	minver	3
%define	pak	pak64

Summary:	A complete Simutrans game data package with 64x64 tiles
Name:		simutrans-%{pak}
Version:	0.%{majver}.%{minver}
Release:	1
License:	Artistic
Group:		Games/Strategy
URL:		http://www.simutrans.com
BuildArch:	noarch
Source0:	http://tenet.dl.sourceforge.net/project/simutrans/%pak/%majver-%minver/simu%pak-%majver-%minver.zip
Provides:	simutrans-pak = %EVRD
Requires:	simutrans

%description
This is a complete data package for Simutrans transport game
with 64x64 tiles.

%prep
%setup -q -c %{name}-%{version}
# All permissions in the zipfile are set to 0000...
# probably packaged by a Windozer!
chmod 0755 . simutrans simutrans/pak
chmod 0755 simutrans/pak/*
chmod 0755 simutrans/pak/*/*
chmod 0755 simutrans/pak/*/*/*
find . -type f |xargs chmod 0644

%install
mkdir -p %{buildroot}%{_datadir}/simutrans
cp -pr simutrans/* %{buildroot}%{_datadir}/simutrans/

%files
%{_datadir}/simutrans/*
