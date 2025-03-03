# Product Preference Prediction System  

## 📅 Current Date : 
**Monday, March 03, 2025**


## 📖 Overview
This project aims to develop a system that predicts whether a user will like a product based on its features and reviews. The goal is to enhance personalized recommendations and increase sales for e-commerce platforms.

## ❓ Problem Statement
E-commerce platforms face challenges in helping users navigate millions of products to find items they like. Current systems lack the ability to predict user preferences based on product features and reviews, which limits personalized recommendations and sales growth.

## 💡 Proposed Solution
The proposed solution is to build a **binary classification model** that predicts whether a user will like a product (1) or not (0). The model will leverage features such as:
- 🏷️ Product price  
- ⭐ Ratings  
- 📂 Category  
- 💸 Discount percentage  
- 📝 User review sentiment  

This system aims to improve personalized recommendations and drive sales by better understanding user preferences.

## 🗂️ Project Structure
The project is organized into the following directories and files:

- **src/**: Contains all the source code files.
  - **components/**: Contains various components of the system.
    - `data_ingestion.py`: Handles data ingestion tasks.
    - `data_transformation.py`: Responsible for transforming the raw data into usable formats.
    - `model_trainer.py`: Includes code to train machine learning models.
    - `model_evaluation.py`: Contains code to evaluate the model's performance.
  - **pipelines/**: Holds the pipeline definitions for training and prediction.
    - `training_pipeline.py`: Defines the pipeline for training the model.
    - `prediction_pipeline.py`: Defines the pipeline for making predictions using the trained model.
  - `logger.py`: Contains the logging mechanism for the project.
  - `exception.py`: Handles custom exception handling.
  - **utils/**: Contains utility functions.
    - `utils.py`: Utility functions that are used across various components.
  - `__init__.py`: Marks the directory as a Python package.

- **experiment/**: Contains experiments related to model evaluation and prototyping.
  - `experiments.ipynb`: Jupyter notebook for running and analyzing experiments.

- **requirements.txt**: Contains the list of dependencies required for the project.
- **requirements_dev.txt**: Contains development dependencies (e.g., for testing, linting).
- **.gitignore**: Specifies which files and directories to ignore in version control.
- **.github/workflows/main.yaml**: GitHub Actions workflow configuration for CI/CD.


## ⚙️ Setup Instructions
1. Clone the repository.  
2. Run `./init_setup.py` to create the necessary directories and files.  
3. Install dependencies listed in `requirements.txt`.  

## 📅 Current Date
This is where the current date is displayed: **Monday, March 03, 2025**.

## 🤝 Contributing
Contributions are welcome! Please submit pull requests with detailed explanations of changes.

