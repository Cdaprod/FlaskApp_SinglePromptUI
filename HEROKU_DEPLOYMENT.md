To deploy the application on Heroku, you'll need a few additional files:

1. `requirements.txt`: This file lists the Python packages required for the application.

2. `Procfile`: This file tells Heroku how to run your application.

3. `runtime.txt`: This file specifies the Python version to use.

Create the following files in your project directory:

**requirements.txt**

```
Flask==2.1.1
waitress==2.1.1
requests==2.27.1
```

**Procfile**

```
web: python app.py
```

**runtime.txt**

```
python-3.9.9
```

Make sure you've committed these new files to your Git repository. Now, follow these steps to deploy the application to Heroku:

1. Sign up for a Heroku account at https://www.heroku.com/ if you don't have one already.

2. Install the Heroku CLI on your computer: https://devcenter.heroku.com/articles/heroku-cli

3. Log in to your Heroku account using the Heroku CLI:

```bash
heroku login
```

4. Create a new Heroku app:

```bash
heroku create your-app-name
```

Replace `your-app-name` with a unique name for your application.

5. Set the Hugging Face API key as a Heroku config variable:

```bash
heroku config:set HUGGINGFACE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Hugging Face API key.

6. Deploy the application to Heroku:

```bash
git push heroku main
```

(If your default branch is named `master` instead of `main`, replace `main` with `master` in the command above.)

7. Open the deployed application in your web browser:

```bash
heroku open
```

Your application should now be running on Heroku, using the secure environment variable for the Hugging Face API key.