#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6SMTP
%define devname %mklibname KPim6SMTP -d

Name: plasma6-ksmtp
Version:	25.08.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/ksmtp/-/archive/%{gitbranch}/ksmtp-%{gitbranchd}.tar.bz2#/ksmtp-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/ksmtp-%{version}.tar.xz
%endif
Summary: KDE library for SMTP mail transmission
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: boost-devel
BuildRequires: sasl-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
Requires: plasma6-akonadi-contacts
# Renamed after 6.0 2025-05-25
%rename plasma6-ksmtp

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE library for SMTP mail transmission.

%package -n %{libname}
Summary: KDE library for SMTP mail transmission
Group: System/Libraries
Requires: %{name} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft
Obsoletes: %{mklibname kpimsmtp 5}

%description -n %{libname}
KDE library for SMTP mail transmission.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft
Obsoletes: %{mklibname -d kpimsmtp}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ksmtp.categories

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
