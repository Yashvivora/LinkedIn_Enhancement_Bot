import streamlit as st
from scraper import scrape_linkedin_profile
from database import store_profile_data
from feedback_generator import generate_feedback, generate_improved_content

def main():
    """
    Main function to run the Streamlit app.
    Allows the user to input a LinkedIn profile URL, scrape the profile, and display feedback & improvements.
    """
    st.title("LinkedIn Enhancement Bot")  # Display the app title

    # Input field for LinkedIn profile URL
    url = st.text_input("Enter LinkedIn Profile URL:")

    # Button to trigger profile enhancement
    if st.button("Enhance Profile"):
        profile_data = scrape_linkedin_profile(url)  # Scrape the LinkedIn profile data

        # Check if the profile was successfully scraped
        if profile_data:
            store_profile_data(url, profile_data)  # Store the scraped data in the database
            st.write("Profile Data Scraped Successfully!")  # Display success message

            # Generate feedback and improved content for the profile sections
            feedback = generate_feedback(profile_data)
            improved_content = generate_improved_content(profile_data)

            # Display feedback and improved content for each section
            st.subheader("Feedback and Suggested Improvements")
            for section, content in feedback.items():
                st.write(f"### {section.capitalize()} Section")
                st.write("**Feedback:**", content)
                st.write("**Improved Content:**", improved_content[section])
        else:
            st.write("Failed to scrape the profile. Please try again.")  # Display error message if scraping failed

if __name__ == "__main__":
    main()  # Run the app
