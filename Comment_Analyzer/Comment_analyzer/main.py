from transformers import pipeline
import streamlit as st

# Initialize the pipeline for text classification
classifier = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Function to classify a comment
def classify_comment(comment):
    result = classifier(comment)[0]['label']
    return result

# Function to display comments
def display_comments(comments, sort_option):
    sorted_comments = []
    if sort_option == "Positive":
        sorted_comments = [comment for comment in comments if comment['classification'] == 'POSITIVE']
    elif sort_option == "Negative":
        sorted_comments = [comment for comment in comments if comment['classification'] == 'NEGATIVE']
    elif sort_option == "None":
        sorted_comments = comments
    
    for idx, comment in enumerate(sorted_comments):
        comment_text = comment['comment']
        classification = comment['classification']
        
        # Determine background color based on sentiment
        background_color = 'lightblue' if classification == 'POSITIVE' else 'lightcoral'
        
        # Generate HTML for comment box with styling
        comment_html = f"""
        <div style="box-shadow: 2px 2px 5px rgba(0,0,0,0.2); margin-bottom: 10px; background-color: {background_color}; border-radius: 5px; padding-left:25px; padding-top:20px; padding-bottom:20px;">
            <p style="font-weight: bold;">USERNAME</p>
            <p>{comment_text}</p>
        </div>
        """
        
        # Display the comment using HTML
        st.write(comment_html, unsafe_allow_html=True)

# Main Streamlit app
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

st.title("Comment Analyzer")

# Text input for entering a comment
comment = st.text_input("Enter your Comment", value="Good")

# Button to add the comment
if st.button("Add Comment"):
    comment_dic = {'comment' : comment, 'classification': classify_comment(comment)}
    st.session_state['all_comments'].append(comment_dic)

# Select box for sorting comments
sort_option = st.selectbox("Sort Comments By:", ["None","Positive", "Negative"])

# Display comments based on the selected sorting option
display_comments(st.session_state['all_comments'], sort_option)
