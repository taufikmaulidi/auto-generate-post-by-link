import os
import google.generativeai as genai
from appapikey import google_gemini_api_key,openai_api_key
import streamlit as st

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

st.set_page_config(layout='wide')
st.title("Auto Generate Artikel")
st.subheader('by gudanginformatika.com')

with st.sidebar:
    st.title('Generate Artikel')
    st.subheader("Isi Url dibawah untuk generate")
    url_artikel = st.text_input('Link Artikel referensi')

    # blog_keywords = st.text_area('Keywords(Saperated with commas)')
    num_len = st.slider("Length of Words", min_value=250, max_value= 1000, step=250)
    # pic_len = st.number_input("Number Of Images",min_value=1, max_value=5, step=1)

    input_promt = [f"anda adalah seorang seo spesialis, anda sudah berpengalaman dalam membuat artikel seo yang gampang di index mesin pencarian. hasil penulisan anda memiliki daya tarik yang tinggi untuk setiap pembaca. saya ingin anda membantu saya untuk membantu saya dalam membuat artikel di blog saya yang beralamat di gudanginformatika.com, blog saya berfokus pada niche atau topik teknologi, gadget. nantinya saya akan memberikan link artikel sebagai referensi anda untuk menulis artikel blog. tugas anda adalah membuat judul yang di modifikasi sesuai teknik seo judul tidak boleh sama dengan judul artikel yang menjadi referensi, selanjutnya anda menuliskan artikel blog dengan referensi link yang saya berikan. usahakan tidak sama agar tidak terindikasi artikel plagiat dan link asli tidak di tampilkan. artikel harus \"{num_len} kata. Link \"{url_artikel}"]

    response = model.generate_content(input_promt)
    # Submit Button 
    submit_button = st.button('Generate Blog')



if submit_button:
    st.write(response.text)