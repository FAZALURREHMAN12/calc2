import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Perform basic arithmetic operations.")

    # Input fields for the numbers
    num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

    # Select the operation
    operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Perform the calculation
    result = None
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")

    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
