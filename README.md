# crm_app

This repository contains the source code for a Customer Relationship Management (CRM) application. The CRM application is built using Django, a high-level Python web framework, and is designed to help businesses manage interactions with current and potential customers.

## Features

- **User Authentication**: Secure authentication system for users to log in and manage their accounts.
- **Customer Management**: Allows users to create, update, and delete customer records.

## Installation

To run the CRM application locally, follow these steps:

1. **Clone this repository** to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:

   ```bash
   cd crm_app
   ```

3. **Set up the virtual environment**:

   ```bash
   python3 -m venv crm_venv
   ```

4. **Activate the virtual environment**:

   ```bash
   source crm_venv/bin/activate
   ```

5. **Install required dependencies** (if a `requirements.txt` file exists):

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** If you don’t have `requirements.txt`, you can create it by running:
   > ```bash
   > pip freeze > requirements.txt
   > ```

6. **Apply the database migrations**:

   ```bash
   python manage.py migrate
   ```

7. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

8. **Access the CRM application** in your web browser at `http://localhost:8000`.

---

## Usage with Makefile Commands

To streamline common project tasks, you can use the provided `Makefile` commands:

- **Set up the environment and install dependencies**:
  ```bash
  make setup
  ```

- **Run the development server**:
  ```bash
  make runserver
  ```

- **Lint your code**:
  ```bash
  make lint
  ```

- **Clean up cache files**:
  ```bash
  make clean
  ```


## Usage

1. **User Registration/Login**: Create a new account or log in with existing credentials.
2. **Customer Management**: Add new customers, update their information.

## Contributing

Contributions are welcome! If you'd like to contribute to the development of this CRM application, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature/my-feature
   ```
5. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for the Django web framework.
- [Bootstrap](https://getbootstrap.com/): Front-end framework for building responsive and mobile-first websites.
- [Font Awesome](https://fontawesome.com/): Icon library for use with web projects.
  
Feel free to update and customize this README file further to suit your project's specific requirements!