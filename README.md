# Spotipy Python API

### Prerequisites

- You will need a Spotify account (free or premium) and a Spotify Developer account. You can sign up for a Spotify Developer account [here](https://developer.spotify.com/dashboard/login). Once you have created an account, create a new app and make note of the Client ID and Client Secret. You will need these later.

- You will need Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).


### Installation

1. Clone the repo
   ```sh
   git clone
   ```

2. You will need to create a `.env` file in the root directory of the project. This file will contain the Client ID and Client Secret that you obtained from Spotify. The file should look like this:
    ```sh
    client_id=your_client_id
    client_secret=your_client_secret
    redirect_url='http://localhost:8000/'
    ```

3. Run `docker-compose up` or, alternatively if you do not want output in your terminal, run `docker-compose up -d`.