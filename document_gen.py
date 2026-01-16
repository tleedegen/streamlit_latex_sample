import streamlit as st
from pylatex import Document, Section, Subsection, Command

def generate_hello_world(sample_text: str="Hello World!"):
    # Create a new document
    doc = Document('hello_world')

    # Add a section 
    with doc.create(Section('This is a LaTeX generated PDF')):
        doc.append(sample_text)
        
        with doc.create(Subsection('A subtitle')):
            doc.append('This PDF was generated using Python and PyLaTeX.')

    # Generate PDF (this will create hello_world.pdf and hello_world.tex)
    
    return doc.generate_pdf(clean_tex=False)

if __name__ == '__main__':
    generate_hello_world()

if 'sample_doc' not in st.session_state:
    st.session_state['sample_doc'] = None
if 'sample_text' not in st.session_state:
    st.session_state['sample_text'] = "Hello World!"

st.title("LaTeX PDF Generator")

st.text_input("Enter text to include in the PDF:", key='sample_text')

if st.button("Generate Hello World PDF"):
    st.session_state["sample_doc"] = generate_hello_world(st.session_state['sample_text'])
    st.success("PDF generated successfully! Check the project directory for 'hello_world.pdf'.")

if st.session_state['sample_doc']:
    st.download_button(
        label="Download Hello World PDF",
        data=st.session_state['sample_doc'],
        file_name="hello_world.pdf",
        mime="application/pdf")
