Summary:	A friendly onboarding wizard for Plasma
Name:		plasma-welcome
Version:	5.27.7
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/plasma-welcome
Source0:	http://download.kde.org/stable/plasma/%(echo %{version}|cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	pkgconfig(Qt5QuickControls2)

%description
A Friendly onboarding wizard for Plasma.
Welcome Center is the perfect introduction
to KDE Plasma! It can help you learn how to
connect to the internet, install apps,
customize the system, and more!

%prep
%autosetup -p1
%cmake_kde5 -DBUILD_TESTING=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang plasma-welcome

%files -f plasma-welcome.lang
%license LICENSES/*
%{_sysconfdir}/xdg/autostart/org.kde.plasma-welcome.desktop
%{_bindir}/plasma-welcome
%dir %{_libdir}/qt5/qml/org/kde/plasma/welcome
%{_libdir}/qt5/qml/org/kde/plasma/welcome/*.qml
%{_libdir}/qt5/qml/org/kde/plasma/welcome/qmldir
%{_datadir}/applications/org.kde.plasma-welcome.desktop
%{_datadir}/metainfo/org.kde.plasma-welcome.appdata.xml
