# video-library

A Web server which gives list and search functions for videos based on a query (india cricket). A background job populates the database. The project is built with Django, DRF and Celery.




## Installation steps

This project can run with Python3.8+

1. Change the .env file at path - `video_library/video_library/.env`
2. Run `docker-compose up --build`
3. The server will be up and running on 8000 port



## Testing the APIs
1. List API - Open http://127.0.0.1:8000/videos/list/ 
2. Pagination list API - http://127.0.0.1:8000/videos/list/?page=2
2. Search API - http://127.0.0.1:8000/videos/search/?query=rohit+sharma


## Bonus features
1. You can keep multiple api keys in .env file by separating them with comma. 
2. Login to admin portal - http://127.0.0.1:8000/admin/api/video/ and you can find a dashboard of all videos
3. Partial match for seach API is supported


## Screenshots
List API
![Alt text](./screenshots/list.png "List API")

Search API
![Alt text](./screenshots/search.png?raw=true "Search API")


Dashboard
![Alt text](./screenshots/dashboard.png?raw=true "Dashboard")
