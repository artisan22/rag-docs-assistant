# Database Runbook

## How to handle database failover
1. Check if primary is down: `pg_isready -h primary`
2. Promote replica: `pg_ctl promote -D /var/lib/postgresql/data`
3. Update connection string in app config
4. Restart application services
5. Notify team in Slack #incidents

## How to restore from backup
1. Stop all application services
2. Run `pg_restore -d mydb backup.dump`
3. Verify data integrity
4. Restart services