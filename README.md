# 数据集来源

数据集来自 `https://spamassassin.apache.org/old/publiccorpus/`

# Email Classifier

This project uses a Transformer model to classify emails as spam or ham.

## Setup with Conda

1. Ensure you have Anaconda or Miniconda installed.

2. Clone this repository:
   ```
   git clone <repository-url>
   cd email_classifier
   ```

3. Create and activate the Conda environment:
   ```
   conda env create -f environment.yml
   conda activate email_classifier
   ```

4. Run the setup script:
   ```
   python setup.py
   ```

## Running the Project

After setting up, you can run the project using:

```
python main.py
```

This will process the data, train the model, and evaluate its performance.

## Project Structure

- `data_processor.py`: Handles data loading and processing
- `data_preprocessor.py`: Prepares data for the model
- `model.py`: Defines the Transformer model
- `trainer.py`: Contains the model training logic
- `evaluator.py`: Evaluates the trained model
- `main.py`: Orchestrates the entire process
- `setup.py`: Sets up the project environment
- `environment.yml`: Defines the Conda environment

## Requirements

See `environment.yml` for a list of dependencies.