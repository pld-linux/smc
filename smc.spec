# TODO:
# - fails on start:
#   CEGUI::Exception: DynamicModule::DynamicModule - Failed to load module
#         'libCEGUIFreeImageImageCodec.so': libCEGUIFreeImageImageCodec.so:
#          cannot open shared object file: No such file or directory
#   CEGUI Exception occurred : DynamicModule::DynamicModule - Failed to load module
#   'libCEGUIFreeImageImageCodec.so': libCEGUIFreeImageImageCodec.so:
#   cannot open shared object file: No such file or directory
#   lib is on libCEGUIFreeImageImageCodec.so.0 - anybody could help with this?
# - pl summary, description and comment (in .desktop)
# - music pack: http://downloads.sourceforge.net/smclone/SMC_music_4.0_high.zip
Summary:	A jump-and-run game similar to classic sidescroller games
Name:		smc
Version:	1.3
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
# Source0-md5:	bbb3eb3b3d96dc542fc71173916f0256
Source1:	%{name}.desktop
URL:		http://www.secretmaryo.org/
BuildRequires:	CEGUI-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	boost-filesystem-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secret Maryo Chronicles is an Open Source two-dimensional platform
game with a style designed similar to classic sidescroller games. It
uses the platform independent library SDL and, since version 0.98, the
OpenGL accelerated Graphics Renderer. The game is developed in C++.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desktop file
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
