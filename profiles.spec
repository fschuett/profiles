Name:          profiles
Summary:       Benutzerprofile
Requires:      kdebase4-runtime plasma5-workspace plasma5-defaults-openSUSE
BuildArch:     noarch
Version:       5.18
Release:       1
License:       GPL
Group:         application
Source:        %{name}-%{version}.tar.gz
Packager:      fschuett
Distribution:  openSUSE Linux
Prefix:        /var/lib/kde-profiles
Url:           http://www.kdekiosk.org


%description
Benutzerprofile für openSUSE Linux mit KDE >= %{version}

%package gymhim
Summary:       Benutzerprofileinstellungen für das Gymnasium Himmelsthür
BuildArch:     noarch
Requires:      schule-kde >= %{version} schule-kde-gymhim >= %{version}

%description gymhim
Benutzerprofile am Gymnasium Himmelsthuer für openSUSE Linux
mit KDE >= %{version}

%package sas
Summary: Benutzerprofileinstellungen für die Sankt-Ansgar-Schule
BuildArch:     noarch
Requires:      schule-kde >= %{version} schule-kde-sas >= %{version}

%description sas
Benutzerprofile an der Sankt-Ansgar-Schule für openSUSE Linux
mit KDE >= %{version}

%prep
%setup -q

%build
# nichts zu tun

%install
mkdir -p %{buildroot}%{prefix}
for d in $(ls -d); do
  mkdir -p %{buildroot}%{prefix}/$d
  cp -aR  $d/* %{buildroot}%{prefix}/$d
done

install -D kde-user-profile-gymhim %{buildroot}/etc/kde-user-profile-gymhim
install -D kde-user-profile-sas %{buildroot}/etc/kde-user-profile-sas
install -D zzz-kde-user-profile.sh %{buildroot}/etc/profile.d/zzz-kde-user-profile.sh

%post gymhim -f %{name}-gymhim.postin

%post sas -f %{name}-sas.postin

%preun gymhim -f %{name}.preun

%preun sas -f %{name}.preun

%postun gymhim -f %{name}.postun

%postun sas -f %{name}.postun

%clean

%files
%defattr(644,root,root,0755)
/etc/profile.d
/var/lib/kde-profiles

%files gymhim
%defattr(644,root,root,0755)
/etc/kde-user-profile-gymhim

%files sas
%defattr(644,root,root,0755)
/etc/kde-user-profile-sas

%changelog
