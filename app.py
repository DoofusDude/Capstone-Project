import streamlit as st

# Define function to create page 1
def page1():
    st.title("Page 1")
    st.write("This is page 1")

# Define function to create page 2
def page2():
    st.title("Page 2")
    st.write("This is page 2")

# Define main function to run the app
def main():
    st.sidebar.title("Navigation")
    pages = {
        "Page 1": page1,
        "Page 2": page2,
    }
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
