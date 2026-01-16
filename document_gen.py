import streamlit as st
from pylatex import Document, Section, Subsection

def generate_hello_world(sample_text: str="Hello World!"):
    #Create the document
    doc = Document('hello_world')
    with doc.create(Section('This is a LaTeX generated PDF')):
        doc.append(sample_text)
        with doc.create(Subsection('A subtitle')):
            doc.append('This PDF was generated using Python and PyLaTeX.')

    doc.generate_pdf('hello_world', clean_tex=True)
    
    #Read the generated file back as binary data
    with open("hello_world.pdf", "rb") as f:
        pdf_data = f.read()
    
    return pdf_data

st.title("LaTeX PDF Generator")

sample_text = st.text_input("Enter text to include in the PDF:", value="Hello World!")

if st.button("Generate Hello World PDF"):
    pdf_bytes = generate_hello_world(sample_text)
    st.session_state["pdf_bytes"] = pdf_bytes
    st.success("PDF generated successfully!")


# Check if we have bytes in session state to enable the download button
if "pdf_bytes" in st.session_state:
    st.download_button(
        label="Download Hello World PDF",
        data=st.session_state["pdf_bytes"],
        file_name="hello_world.pdf",
        mime="application/pdf"
    )