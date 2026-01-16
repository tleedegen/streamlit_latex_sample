import streamlit as st
from pylatex import Document, Section, Subsection, Command

def generate_hello_world():
    # Create a new document
    doc = Document('hello_world')

    # Add a section
    with doc.create(Section('This is a LaTeX generated PDF')):
        doc.append('Hello World!')
        
        with doc.create(Subsection('A subtitle')):
            doc.append('This PDF was generated using Python and PyLaTeX.')

    # Generate PDF (this will create hello_world.pdf and hello_world.tex)
    doc.generate_pdf(clean_tex=False)
    return doc

if __name__ == '__main__':
    generate_hello_world()


st.title("LaTeX PDF Generator")
if st.button("Generate Hello World PDF"):
    st.session_state["sample_doc"] = generate_hello_world()
    st.success("PDF generated successfully! Check the project directory for 'hello_world.pdf'.")

st.download_button(
    label="Download Hello World PDF",
    data=st.session_state['sample_doc'],
    file_name="hello_world.pdf",
    mime="application/pdf")
