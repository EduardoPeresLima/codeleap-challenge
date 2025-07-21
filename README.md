# CodeLeap Challenge
## Deploy URL
- https://codeleap-challenge-api.onrender.com/
## Endpoints available
- **Endpoints** (There is a [Postman JSON attached](CodeLeap.postman_collection.json))
  - **Posts**
    - Fetch All Posts: `GET /careers/`
    - Create Post: `POST /careers/`
    - Update Post: `PATCH /careers/{post_id}/`
    - Delete Post: `DELETE /careers/{post_id}/`
  - **Comments**
    - Fetch All Comments for a Post: `GET /careers/{post_id}/comments/`
    - Create Comment for a Post: `POST /careers/{post_id}/comment/`
    - Create Nested Comment for a post: `POST /careers/{post_id}/comment/` (with `parent_comment` field)
    - Update Comment: `PATCH /careers/comment/{comment_id}/`
    - Delete Comment: `DELETE /careers/comment/{comment_id}/`

## Additional Work

- Used PostgreSQL as the database instead of the default SQLite
- Added Dockerfile and Docker Compose configuration to easily run the application locally and in deployment environments
- Implemented functionality to add comments to posts, as well as nested comments (comments on comments)

## How to use the postman collection
1. Import the attached **Postman collection** `CodeLeap.postman_collection.json`.
2. Set the **`ENVIRONMENT`** variable in Postman to `LOCAL` or `PROD`.
    - `LOCAL`: `http://127.0.0.1:8000`
    - `PROD`: `https://codeleap-challenge-api.onrender.com`
3. Use the provided endpoints for CRUD operations on posts and comments.
    

### Run locally on docker
- Clone the repo with `git clone https://github.com/EduardoPeresLima/codeleap-challenge.git`
- Open terminal on the repo file
- Run `npm run up`