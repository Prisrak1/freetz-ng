. /usr/lib/cgi-bin/mod/modlibcgi

show_log() {
	local log="$1"
	if [ -s "$log" ]; then
		logg=true
		echo "<h1><a href='$SCRIPT_NAME$log'>$log</a></h1>"
		echo "<pre class='log ${class:-small}'>"
		html < "$log" | highlight
		echo '</pre>'
	fi
}

unset class
do_log() {
	show_log "$1"
}

if [ -n "$PATH_INFO" ]; then
	class="full"
	do_log() {
		[ "$PATH_INFO" = "$1" ] && show_log "$1"
	}
fi

case "$3" in
	logs_avm*)
		logg=false

		do_log /proc/avm/log_sd/crash
		do_log /proc/avm/log_sd/crash2
		do_log /proc/avm/log_sd/panic
		do_log /proc/avm/log_sd/panic2

		do_log /var/log/crash2
		do_log /var/log/debug2
		do_log /var/log/panic2

		do_log /var/flash/crash.log
		do_log /var/flash/panic
		do_log /var/log/messages

		do_log /var/log/dslmonitor.txt

		do_log /var/tmp/pbook.err

		do_log /var/tmp/mserv4.log
		do_log /var/tmp/webdav.log

		do_log /var/tmp/cloudcds.log
		do_log /var/tmp/lgpm.log
		do_log /var/tmp/tcloud.log

		$logg || echo "<br><h1>$(lang de:"Keine Logdateien gefunden" en:"No log files found")!</h1>"
		;;
	*)
		do_log /var/log/mod_load.log
		do_log /var/log/mod_net.log
		do_log /var/log/mod_voip.log
		do_log /var/log/mod.log
		do_log /var/log/mod_swap.log
		do_log /var/log/rc_custom.log
		do_log /var/log/debug_cfg.log
		do_log /var/log/onlinechanged.log
		do_log /var/log/external.log
		do_log /var/log/mod_mount.log
		;;
esac

