# CSV File Uploader

## Overview

The CSV File Uploader is a web application designed for users to manage and work with CSV files effortlessly. It includes user registration and authentication, CSV file upload, and data processing features to enhance data management capabilities.

## Key Features

1. **User Registration and Authentication**: Utilizes the [allauth](https://django-allauth.readthedocs.io/en/latest/) package to enable user account creation, login, and secure access control for the CSV uploader.

2. **CSV File Upload**: Users can easily upload CSV files with comma-separated values via an intuitive web interface.

3. **Data Processing**: Offers a range of data manipulation options for the uploaded CSV files, including filtering, sorting, and more.

## Getting Started

To set up and run the CSV File Uploader locally, follow these steps:

**Clone the Repository**:
   git clone [repository_url]

**Navigate to the Project Directory**:
   cd csv-uploader-project

**Create a Virtual Environment**:
  python -m venv myenv

## Activate the Virtual Environment

**On Windows:**
myenv\Scripts\activate

## Install Dependencies

To install the required dependencies, run the following command:
pip install -r requirements.txt

## Database Configuration

Configure database settings in the .env file.
Create a database (e.g., catalyst_db).

**Apply Migrations**:
python manage.py migrate

**Start the Development Server**:
python manage.py runserver

**Configuration**:
Open the project's settings file: 
Ensure that the following apps are included in the INSTALLED_APPS section:
INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    # ... other apps ...
]

## Usage

### User Registration and Login:

1. Register a new account or log in using an existing account.

### CSV Upload:

1. After logging in, navigate to the CSV uploader section.
2. Click the "Upload CSV" button and select the CSV file you want to upload.

### Data Manipulation:

1. Once the file is uploaded, you can perform various operations on the data as needed.
   
