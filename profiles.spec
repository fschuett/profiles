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
/etc
/var/lib/kde-profiles

%files gymhim
%defattr(644,root,root,0755)
/etc/kde-user-profile-gymhim

%files sas
%defattr(644,root,root,0755)
/etc/kde-user-profile-sas

%changelog
* Thu Nov 15 2018 fschuett@gymhim.de
- disable display dimming for netbooks (#x200ma: display flickers)
* Wed Oct 18 2017 fschuett@gymhim.de
- disable 3D effects (not working on slow scieneo)
- correct SAS links
* Wed May 24 2017 fschuett@gymhim.de
- bluetooth device blocked only for klassenarbeit on netbook
- baloo file indexing disabled
* Tue Apr 11 2017 fschuett@gymhim.de
- add default profile
* Wed Feb 1 2017 fschuett@gymhim.de
- disable kscreenlocker
- hibernate on power button
- klassenarbeit-Schema
* Thu Jan 12 2017 fschuett@gymhim.de
- update to KDE 5.8
- reactivate auto mounting
* Mon Feb 22 2016 fschuett@gymhim.de
- add klassenarbeitwaechter to ksmserverrc
* Mon Feb 15 2016 fschuett@gymhim.de
- change domain gymnasium-himmelsthuer.de -> gymhim.de
- proxy settings: use system settings
* Wed Jul 22 2015 fschuett@gymhim.de
- added sas-netbook-klassenarbeit
- added marblerc
* Tue Aug 5 2014 fschuett@gymnasium-himmelsthuer.de
- profiles desktoptheme klassenarbeit
* Mon Aug 4 2014 fschuett@gymnasium-himmelsthuer.de
- AutomountUnknownDevices=true, KDE Bug #261376
* Sat Aug 2 2014 fschuett@gymnasium-himmelsthuer.de
- USB Automount eingeschaltet
- AutomountUnknowDevices hat die Bedeutung von DontAutomountUnknownDevices
* Tue Dec 3 2013 fschuett@gymnasium-himmelsthuer.de
- Tastaturlayout (siehe #488)
* Thu Nov 14 2013 fschuett@gymnasium-himmelsthuer.de
- Klassenarbeitsmodus: zusätzliches Profil für den Benutzer klassenarbeit
* Sun Sep 22 2013 fschuett@gymnasium-himmelsthuer.de
- gymhim.netbook: nepomukserverrc Start Nepomuk=fals wegen Abstürzen
* Mon Sep 16 2013 fschuett@gymnasium-himmelsthuer.de
- Energieverwaltung ist jetzt in powermanagementprofilesrc
* Sat Jun 8 2013 fschuett@gymnasium-himmelsthuer.de
- added gymhim-netbook netbook shell autostart for user schueler
- numlock aus für netbook
- Bildschirm herunterklappen -> Bildschirm aus, kein Ruhezustand wegen Scieneo-Absturz
* Fri May 31 2013 fschuett@gymnasium-himmelsthuer.de
- added 2 netbook profiles: gymhim-netbook, sas-netbook
- updated to KDE 4.10.2
- added tmp.conf
- added gymhim-netbook-wallpaper use in config files
* Fri Mar 9 2012 fschuett@gymnasium-himmelsthuer.de
- removed ksmserverrc restartSession
* Tue Feb 28 2012 fschuett@gymnasium-himmelsthuer.de
- removed mysql-global.conf (switch akonadi to sqlite3)
* Thu Feb 9 2012 fschuett@gymnasium-himmelsthuer.de
- adapted to KDE 4.7.2
* Tue Nov 15 2011 fschuett@gymnasium-himmelsthuer.de
- add TMP* variables to clear to postin script
- remove doubled cron.daily.local (suse.de-clean-tmp does it)
* Thu Jul 7 2011 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- create subpackages sas gymhim
* Fri Nov 19 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- fixed post,postun
- removed device manager from profile
- changed settings to auto mount
* Fri Jun 04 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- add cron.daily.local to clean symlinks and pipes from tmp
* Wed May 26 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- added FloatingTools to ksmserverrc
* Tue May 04 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- ksmserverrc: processes renamed for smartsoftware 10.2.321
* Thu Jan 14 2010 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- Effekte unter KDE4 abschalten (nicht zwingend)
- add switch $1=1 to postin script
* Sat Dec 12 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- powerdevilrc für Lehrer hinzugefügt
- ksmserver shutdownType=2 für alle hinzugefügt
- Variable für postun hinzugefügt
* Thu Dec 08 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- showLockButton=false in plasma-desktop...
- ksmserver smartboard-Ausnahme hinzugefügt für alle
- kcmdisplayrc, kscreensaverrc für Lehrer modifiziert
* Thu Sep 11 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- postin- / postun-Skripte korrigiert (kde4rc geaendert)
- neue Zertifikate und Bookmarks(Firefox) importiert
* Thu Sep 10 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- /etc/akonadi/mysql-global.conf wird angepasst
- neue Vorbedingung: akonadi-runtime
* Tue Sep 1 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- Akonadi-Migration abgeschaltet mit kres-migratorrc
