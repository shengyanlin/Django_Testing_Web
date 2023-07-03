# README.md

This README file outlines the steps for setting up and running the web application on your local machine.

## 1. Creating a Virtual Environment

The first step is to create a virtual environment to isolate our project dependencies. Here we use Conda, which is a package manager, and an environment manager. If you haven't installed Conda, please follow the installation steps provided [here](https://docs.anaconda.com/anaconda/install/).

To create a Conda environment, please use the following command:

```bash
conda create --name myenv
```

Here `myenv` is the name of your new environment. You can replace it with any name you like. 

Activate the environment using:

```bash
conda activate myenv
```

## 2. Installing Required Packages

Now, we will install the necessary packages for the project. You should have a `requirements.txt` file in your project root directory containing a list of required packages.

Use the following command to install the packages:

```bash
pip install -r requirements.txt
```

Make sure you're running this command from the directory where `requirements.txt` is located.

## 3. Running the Web Application Locally

To run this web application locally, use the following command:

```bash
python manage.py runserver
```

Your web application will be running at `http://127.0.0.1:8000/`.

## 4. Running the Web Application for Public Access

If you want to run this web application such that everyone can access it, you can use ngrok, a tool that exposes local servers to the public internet.

Use the following command:

```bash
ngrok http <number-of-your-port>
```

Replace `<number-of-your-port>` with the port number your server is running on.

That's it! You're all set to run the application. Enjoy developing!
