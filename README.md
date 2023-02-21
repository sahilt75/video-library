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
<img width="1361" alt="image" src="https://user-images.githubusercontent.com/21974202/220396822-cb249ca3-0afe-49e0-a693-d945f7e457ea.png">

Search API
<img width="1340" alt="image" src="https://user-images.githubusercontent.com/21974202/220396982-33a6be1f-dbe3-4bae-a623-d3913eb234b7.png">

Dashboard
<img width="1503" alt="image" src="https://user-images.githubusercontent.com/21974202/220396769-55ac914b-933e-4366-8ad1-99620b3bb59f.png">
