import nbformat as nbf
import pandas as pd
from datetime import datetime
import os

def create_daily_report(data_filepath):
    try:
        # Load the data
      df = pd.read_csv(data_filepath)

      # Create a new notebook
      nb = nbf.v4.new_notebook()

      # Add basic analysis code to the notebook
      basic_analysis_code = f"""
        import pandas as pd
        import matplotlib.pyplot as plt

        # Load data
        df = pd.read_csv("{data_filepath}")

        # Basic descriptive statistics
        print("Descriptive Statistics:")
        print(df.describe())

        # Plot price trends
        plt.figure(figsize=(10, 6))
        df['current_price'].plot(title="Daily Price Trend")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()
        """
      nb.cells.append(nbf.v4.new_code_cell(basic_analysis_code))

      # Add forecasting code to the notebook
      forecasting_code = """
        from prophet import Prophet
        import pandas as pd

        # Prepare data for Prophet
        df['ds'] = pd.to_datetime(df['last_updated'])
        df['y'] = df['current_price']

        # Removing timezone from ds column before fitting
        df['ds'] = df['ds'].dt.tz_localize(None)
        
        # Train Prophet model
        model = Prophet()
        model.fit(df)

        # Forecast future values
        future = model.make_future_dataframe(periods=7)  # Predict the next 7 days
        forecast = model.predict(future)

        # Plot forecast
        fig = model.plot(forecast)
        """
      nb.cells.append(nbf.v4.new_code_cell(forecasting_code))

      # Save the notebook in the current directory
      today = datetime.now().strftime('%d-%m-%Y')
      notebook_filename = f'daily_crypto_report_{today}.ipynb'
      notebook_filepath = os.path.join(os.getcwd(), notebook_filename)

      with open(notebook_filepath, 'w') as f:
          nbf.write(nb, f)

      print(f"Notebook saved at: {notebook_filepath}")
      return notebook_filepath

    except Exception as e:
        print("Failed to create the notebook.")
        print(e)
