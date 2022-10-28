# FastAPITuto


# COMMAND LOCAL AND PROD

<!-- CHECK LOGS -->
docker-compose logs -f

## LOCAL :
<!-- BUILD LOCAL -->
- docker-compose up -d --build

<!-- DB LOCAL -->
- docker-compose exec db psql --username=fastapi_traefik --dbname=fastapi_traefik

<!-- DOWN ANY EXISTING CONTAINERS -->
- docker-compose down -v 

## PROD :
<!-- Déployer sur un domaine avec utilisation DNS accesible par ce lien si pas de probleme lors du docker-compose de la PROD -->
<!-- Lien du site -->
fastapi-traefik.fastapi-traefik-gamebase.gq

<!-- Lien du dashboard -->
dashboard-fastapi-traefik.fastapi-traefik-gamebase.gq

<!-- BUILD PROD -->
- docker-compose -f docker-compose.prod.yml up -d --build

<!-- BD PROD -->
- docker-compose exec db psql --username=fastapi_traefik_prod --dbname=fastapi_traefik_prod

<!-- DOWN ANY EXISTING CONTAINERS PROD -->
- docker-compose -f docker-compose.prod.yml down -v

# DOCUMENTATION
<!-- LOCAL -->
http://fastapi.localhost:8008/

<!-- DASHBOARD TRAEFIK -->
http://fastapi.localhost:8081/dashboard/#/

