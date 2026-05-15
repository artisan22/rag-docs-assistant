# Incident Response Runbook

## High memory usage
1. Check which process is consuming memory: `top` or `htop`
2. Check application logs for memory leaks
3. Restart the offending service
4. Alert team if memory stays above 90%

## Disk space critical
1. Check disk usage: `df -h`
2. Find large files: `du -sh /* | sort -rh | head -20`
3. Clear old logs: `journalctl --vacuum-time=7d`
4. Alert team if below 5%