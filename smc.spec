Summary:	A jump-and-run game similar to classic sidescroller games
Summary(pl.UTF-8):	Gra typu "skacz i biegnij" podobna do klasycznych przewijanych gier
Name:		smc
Version:	1.9
Release:	9
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
# Source0-md5:	75ab7826303c49aec25b052a8b90287f
Source1:	http://dl.sourceforge.net/sourceforge/smclone/SMC_Music_4.1_high.zip
# Source1-md5:	f0d5fad6f1d0387bd909c93226698ba9
Source2:	%{name}.desktop
Patch0:		link.patch
URL:		http://www.secretmaryo.org/
BuildRequires:	CEGUI-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
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
%patch -P0 -p1
%{__unzip} -qq -o %{SOURCE1}

%build
export CXXFLAGS="%{rpmcxxflags} -DBOOST_FILESYSTEM_VERSION=2"
%{__aclocal}
%{__automake}
%{__autoconf}
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
