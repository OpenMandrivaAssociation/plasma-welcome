%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	A friendly onboarding wizard for Plasma
Name:		plasma-welcome
Version:	6.4.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/plasma-welcome
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-welcome/-/archive/%{gitbranch}/plasma-welcome-%{gitbranchd}.tar.bz2#/plasma-welcome-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/plasma-welcome-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	pkgconfig(Qt6QuickControls2)
# Renamed after 6.0 2025-05-03
%rename plasma6-welcome

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
A Friendly onboarding wizard for Plasma.
Welcome Center is the perfect introduction
to KDE Plasma! It can help you learn how to
connect to the internet, install apps,
customize the system, and more!

%files -f %{name}.lang
%{_bindir}/plasma-welcome
%{_qtdir}/plugins/kf6/kded/kded_plasma-welcome.so
%{_datadir}/applications/org.kde.plasma-welcome.desktop
%{_datadir}/metainfo/org.kde.plasma-welcome.appdata.xml
%{_libdir}/libplasma-welcome-publicplugin.a
%{_qtdir}/qml/org/kde/plasma/welcome
