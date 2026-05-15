# Deployment Runbook

## How to deploy service X
1. Run `git pull origin main`
2. Run `docker compose pull`
3. Run `docker compose up -d`
4. Check health: `curl http://localhost:8080/health`
5. Monitor logs: `docker compose logs -f`

## Rollback procedure
1. Run `docker compose down`
2. Run `git checkout previous-tag`
3. Run `docker compose up -d`