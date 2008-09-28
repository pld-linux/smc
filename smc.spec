Summary:	A jump-and-run game similar to classic sidescroller games
Summary(pl.UTF-8):	Gra typu "skacz i biegnij" podobna do klasycznych przewijanych gier
Name:		smc
Version:	1.6
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
# Source0-md5:	f3197a5e61c1899637ff1a2a858db226
Source1:	http://dl.sourceforge.net/smclone/SMC_music_4.0_high.zip
# Source1-md5:	bb007603c723eddd6ccb007cc5f01cd6
Source2:	%{name}.desktop
URL:		http://www.secretmaryo.org/
BuildRequires:	CEGUI-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secret Maryo Chronicles is an Open Source two-dimensional platform
game with a style designed similar to classic sidescroller games. It
uses the platform independent library SDL and, since version 0.98, the
OpenGL accelerated Graphics Renderer. The game is developed in C++.

%description -l pl.UTF-8
Secret Maryo Chronicles to mająca otwarty kod źródłowy dwuwymiarowa
gra platformowa w stylu podobnym do klasycznych gier z przewijanym
ekranem. Wykorzystuje niezależną od platformy bibliotekę SDL oraz, od
wersji 0.98, renderer graficzny z akceleracją OpenGL. Gra jest
tworzona w C++.

%prep
%setup -q
/usr/bin/unzip -qq -o /home/users/Arvenil/rpm/SOURCES/SMC_music_4.0_high.zip

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desktop file
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

# icon
cp -f data/icon/window_32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
