# Stock Notifier - Get Email Alerts for Significant Stock Price Changes
This Python script allows you to track selected stocks and receive email alerts whenever the price of a stock increases or decreases by more than 5%.
it will send you then 3 top news of your selected company if the stock changes by more than 5%.

## Prerequisites

Before running the stock notifier, ensure you have the following installed:

- Python (3.x recommended)
-  smtplib and email libraries (for sending email alerts)
-  modify your email and your password in main.py.

You can install the required libraries using pip:

```
pip install smtplib
```

## Setup

1. Clone the repository or copy the script: `main.py` to your local machine.

2. Open the `main.py` file in a text editor.

3. Update the email credentials and settings in the script:

   - `SMTP_SERVER`: Your SMTP server's address.
   - `USERNAME`: Your email address for authentication.
   - `PASSWORD`: Your email account password or an app password (if using Gmail).
   - `FROM_EMAIL`: Your email address (sender).
   - `TO_EMAIL`: The recipient's email address.

4. Add the stock symbol you want to track:

   ```python
   STOCK = "TSLA"
   ```

5. Save the changes.

## Usage

To run the stock notifier, execute the following command in your terminal or command prompt:

```
python main.py
```

The script will fetch the latest stock data for the provided symbols and compare it with the previous day's closing price. If any stock's price has increased or decreased by more than 5%, it will send an email notification containing 3 top news about the stock to the specified email address.

## Disclaimer

This stock notifier is provided for educational purposes only. Stock trading involves financial risk, and it is essential to conduct thorough research and seek advice from a qualified financial advisor before making any investment decisions.

The authors of this script are not responsible for any financial losses or gains resulting from the usage of this script or its derivatives.

---

Feel free to customize this README file based on your specific implementation and any additional features you may add to the stock notifier. Additionally, don't forget to include any necessary information or disclaimers based on your usage and distribution of the script.
