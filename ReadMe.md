## Geting started

### Start Application
1. ```sudo systemctl stop postgresql.service``` - Stop postgres
2. ```docker-compose up --build``` - Build and start application (for initial setup)
3. ```docker-compose up``` - Start app without building (for continuous development)
4. ```docker-compose up -d``` - Start in detachment mode


## Database Management
1. ```docker-compose exec db psql --username=postgres_user --dbname=your_password```
