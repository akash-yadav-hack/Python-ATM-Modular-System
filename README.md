# 🏦 Python ATM Modular System

Welcome to my professional ATM simulation project! This is Phase 2 of my Python learning journey, where I transitioned from a single-file script to a **Modular Architecture**.

### 🚀 Key Features
- **Modular Design**: Separated logic into `bank_logic.py`, `utils.py`, and `main_app.py`.
- **Dynamic OTP**: Secure 4-digit OTP generation for every login attempt.
- **Error Handling**: Uses `try-except` blocks to prevent crashes from invalid inputs.
- **Transaction Logging**: Automatically records every successful login in `Account_details.txt`.

### 📂 File Structure
- `main_app.py`: The entry point of the application (The Controller).
- `bank_logic.py`: Contains the `Account` class and core banking methods.
- `utils.py`: Helper functions for OTP generation and time formatting.

### 🏃 How to Run
1. Clone or download this repository.
2. Ensure you have Python installed.
3. Run the following command in your terminal:
   ```bash
   python main_app.py
