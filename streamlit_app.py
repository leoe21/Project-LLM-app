import streamlit as st
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import os

def generate_response(uploaded_file, openai_api_key, query_text):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if uploaded_file is not None:
        try:
            documents = [uploaded_file.read().decode()]
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.create_documents(documents)
            if not texts:
                return "❌ Error: El documento está vacío o no se pudo procesar."

            embeddings = OpenAIEmbeddings(api_key=openai_api_key)
            db = FAISS.from_documents(texts, embeddings)
            retriever = db.as_retriever()
            qa = RetrievalQA.from_chain_type(
                llm=OpenAI(api_key=openai_api_key),
                chain_type='stuff',
                retriever=retriever
            )
            return qa.run(query_text)
        except Exception as e:
            return f"❌ Error al generar la respuesta: {str(e)}"

# Streamlit app
st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Ask the Doc App')

uploaded_file = st.file_uploader('Upload an article', type='txt')
query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.', disabled=not uploaded_file)

result = []
with st.form('myform', clear_on_submit=True):
    #openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text)) Lo pedia en el frontend
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Calculating...'):
            response = generate_response(uploaded_file, openai_api_key, query_text)
            result.append(response)
            del openai_api_key

if result:
    if result[0].startswith("❌"):
        st.error(result[0])
    else:
        st.info(result[0])
