
# add kde-profile dirs to XDG_DATA_DIRS, XDG_CONFIG_DIRS
# workaround for not working kde profiles
BASEDIR=/var/lib/kde-profiles/

if [ -e /etc/kde-user-profile ]; then
  TEACHERDIRS="$(cat /etc/kde-user-profile|grep '^teachers='|awk -F\= '{ print $2 }'| tr ',' ' ')"
  STUDENTDIRS="$(cat /etc/kde-user-profile|grep '^students='|awk -F\= '{ print $2 }'| tr ',' ' ')"
  SCHUELERDIRS="$(cat /etc/kde-user-profile|grep '^schueler='|awk -F\= '{ print $2 }'| tr ',' ' ')"
  KLASSENARBEITDIRS="$(cat /etc/kde-user-profile|grep '^klassenarbeit='|awk -F\= '{ print $2 }'| tr ',' ' ')"
fi

if [ -n "${TEACHERDIRS}${STUDENTDIRS}${SCHUELERDIRS}${KLASSENARBEITDIRS}" ]; then
  case $USER in
    schueler)
      for dir in $SCHUELERDIRS; do
        test -d "$BASEDIR$dir/share" && XDG_DATA_DIRS="$BASEDIR$dir/share:$XDG_DATA_DIRS"
        test -d "$BASEDIR$dir/config" && XDG_CONFIG_DIRS="$BASEDIR$dir/config:$XDG_CONFIG_DIRS"
      done;
    ;;
    klassenarbeit)
      for dir in $KLASSENARBEITDIRS; do
        test -d "$BASEDIR$dir/share" && XDG_DATA_DIRS="$BASEDIR$dir/share:$XDG_DATA_DIRS"
        test -d "$BASEDIR$dir/config" && XDG_CONFIG_DIRS="$BASEDIR$dir/config:$XDG_CONFIG_DIRS"
      done;
    ;;
    *)
    ;;
  esac
  
  if id -Gn $USER|grep -qiw teachers; then
      for dir in $TEACHERDIRS; do
        test -d "$BASEDIR$dir/share" && XDG_DATA_DIRS="$BASEDIR$dir/share:$XDG_DATA_DIRS"
        test -d "$BASEDIR$dir/config" && XDG_CONFIG_DIRS="$BASEDIR$dir/config:$XDG_CONFIG_DIRS"
      done;
  fi
  
  if id -Gn $USER|grep -qiw students; then
      for dir in $STUDENTDIRS; do
        test -d "$BASEDIR$dir/share" && XDG_DATA_DIRS="$BASEDIR$dir/share:$XDG_DATA_DIRS"
        test -d "$BASEDIR$dir/config" && XDG_CONFIG_DIRS="$BASEDIR$dir/config:$XDG_CONFIG_DIRS"
      done;
  fi
  
  unset TEACHERDIRS STUDENTDIRS SCHUELERDIRS KLASSENARBEITDIRS
  
  export XDG_DATA_DIRS XDG_CONFIG_DIRS
  
fi

unset BASEDIR
