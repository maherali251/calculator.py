import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def perform_calculation(x, y, op):
    if op == '+':
        return add(x, y)
    elif op == '-':
        return subtract(x, y)
    elif op == '*':
        return multiply(x, y)
    elif op == '/':
        return divide(x, y)

def main():
    st.title("welcome to Ali's Calculator")

    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

    operator = st.selectbox("Select operator:", ['+', '-', '*', '/'])

    if st.button("Calculate"):
        if operator == '/' and num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = perform_calculation(num1, num2, operator)
            st.write(f"The result of {num1} {operator} {num2} is: {result}")

    if st.button("Quit"):
        st.stop()

if _name_ == "_main_":
    main()