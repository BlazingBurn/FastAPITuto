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

