
___
# Local Deployment

Prerequisites: 
    
To deploy this project you require the following installed on you local computer or IDE: 
    
- Python 3 or higher - Programming Language
- Pip3 - Python Package Installer
- Git - Version control
___
## Cloning the Repository using Git

1. Open the repository, click the code button, which is located on the right above all the repository file names.
2. Select HTTPS and copy the clone URL.
3. In your command line type "git clone" and then paste the URL that you just copied.
4. Press enter to create your local clone

___
## Cloning the Repository using GitPod
To clone the repository, you first need to:
1. Install the GitPod Browser Extension for Chrome (including restarting the browser).
2. Log into your GitHub or create an account.
3. Find the GitHub Repository that you want to clone.
4. Click the green "GitPod" button in the top right corner of the repository. This will trigger a new GitPod workspace to be created.


The cloned repository includes the ‘requirements.txt’ file. To install all of the packages required for this project to run, use the following command in the terminal:

        pip3 install -r requirements.txt

Once that installation is successful, setup a superuser entering the command below into the terminal and following the prompts:

        python 3 manage.py createsuperuser

___
## Development Environment Variables

The following environment variables must be set within your development environment for the application to function.
| Variable | Value |
| --- | --- |
| DEVELOPMENT | True |
| SECRET_KEY | A randomly generated django secret key |
| STRIPE_PUBLIC_KEY | Value attained from Stripe Account |
| STRIPE_SECRET_KEY | Value attained from Stripe Account |
| STRIPE_WH_SECRET | Value attained from stripe webhook endpoint |

___
## Development Server Database Setup
To set up your projects local database you will need to run migrations by entering the following commands into the CLI and following any prompts, if there are any:

        python3 manage.py migrate --plan python3 manage.py migrate

You should now commit all these changes to the repository.
To run the application locally just enter the command below into the CLI: 
        
        python3 manage.py runserver

___
# Heroku Deployment

To deploy the project to Heroku you need to:
1. Go to Heroku and log into your account. If you do not have one, create one.
2. Click create an app, enter a valid app name, choose the region closest to your location and click
“Create App”.
3. When the app is created, add a Postgres database to it by selecting it from the addons list
4. You will then need to set the following variables in the Heroku “Config Vars”. If you do not have the variable yet, continue on the deployment until you create them.

| Variable | Value |
|---|---|
| SECRET_KEY | A randomly generated django secret key |
| STRIPE_PUBLIC_KEY | Value attained from Stripe Account (see Stripe Setup) |
| STRIPE_SECRET_KEY | Value attained from Stripe Account (see Stripe Setup) |
| STRIPE_WH_SECRET | Value attained from stripe webhook endpoint (see Stripe Setup) |
| DATABASE_URL | automatically setup during Heroku deployment and can be found by viewing your Postgres database within the Heroku dashboard, under Settings Database Credentials |

To have your project automatically deploy to Heroku when you push the repository to Github you need to set up automatic deployment. To do this you need to:
1. Click the deploy tab on your Heroku App.
2. Select GitHub as the deployment method
3. Search for an select the GitHub repo you want to connect to
4. Click “Connect” and then “Enable Automatic Deploys”

___