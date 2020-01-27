# child-track API (Version 0.0.0)

## Author: DeveloperPrince

This is a basic tracking application which keeps track of animals by use of Earth Coordinate System by Retrieving & Updating latitude and longitudinal position of the animals.

The first phase it keeps track of a single animal this is demo project.

## API DOCUMENTATION

| REQUEST |                 END POINT                       |       PARAMETERS          |           RESULTS         |
|---------|-------------------------------------------------|---------------------------|---------------------------|
|  GET    | /animal_tracking_system/api/controllers/locator |                           |                           |
|  POST   | /animal_tracking_system/api/controllers/tracker |  longitude, latitude      |                           |

## SETUP
```bash
python -m venv dev

source dev/bin/activate
```
## RUN
```bash
export FLASK_APP=run.py #linus or unix environment
export FLASK_ENV=development #linux or unix environment

set FLASK_APP=run.py #Win environment
set FLASK_ENV=development #Win environment
```
### start server
```bash
flask run
```
Coming Soon

This Web Application Powered by VillageWork