import streamlit as st
import pytesseract
from PIL import Image
import pdf2image
import re
import tempfile
import os

st.set_page_config(page_title="Extrator de Precatórios - CREAR", page_icon="📄", layout="centered")

# Adiciona logo da Crear
st.image("https://crearativos.com.br/assets/logo-crear.png", width=200)

st.title("📄 Extrator de Dados de Precatórios")
st.markdown("Automatize a leitura de ofícios para alimentar sua plataforma de cotações.")

uploaded_file = st.file_uploader("Envie um arquivo PDF ou imagem (JPG/PNG)", type=["pdf", "jpg", "jpeg", "png"])

def extract_text_from_file(file):
    text = ""
    if file.name.endswith(".pdf"):
        with tempfile.TemporaryDirectory() as path:
            images = pdf2image.convert_from_bytes(file.read(), dpi=300, output_folder=path)
            for image in images:
                text += pytesseract.image_to_string(image, lang='por')
    else:
        image = Image.open(file)
        text = pytesseract.image_to_string(image, lang='por')
    return text

def extract_fields(text):
    data = {}
    data['CPF/CNPJ'] = re.search(r'CPF/CNPJ:\s*(\d{3}\.\d{3}\.\d{3}-\d{2})', text)
    data['Requerente'] = re.search(r'Nome:\s*(.+)', text)
    data['Requerido'] = re.search(r'Executado\(s\):\s*(.+)', text)
    data['Natureza'] = re.search(r'Natureza do crédito:\s*(.+)', text)
    data['Vara'] = re.search(r'VARA DE FAZENDA PÚBLICA.*', text)
    data['Estado'] = "São Paulo" if "SÃO PAULO" in text else ""
    data['Cidade'] = "São Paulo" if "COMARCA DE SÃO PAULO" in text else ""
    data['Data base'] = re.search(r'Data base para atualização:\s*(\d{2}/\d{2}/\d{4})', text)
    data['Data de expedição'] = re.search(r'em\s*(\d{2}/\d{2}/\d{4})\s*às', text)
    data['Número do precatório'] = re.search(r'OFÍCIO REQUISITÓRIO Nº\s*(\d+/\d+)', text)
    data['Número do processo'] = re.search(r'Processo nº:\s*([\d\.-/]+)', text)
    data['Descontos'] = ", ".join(re.findall(r'([A-Z\.\-\s]+)\s+R\$\s*([\d\.,]+)', text))
    data['RRA (meses)'] = "n/c" if "RRA" not in text else "informar"

    for key in data:
        if data[key] and hasattr(data[key], 'group'):
            data[key] = data[key].group(1).strip()
    return data

if uploaded_file:
    with st.spinner("🔍 Extraindo texto do documento..."):
        raw_text = extract_text_from_file(uploaded_file)
        fields = extract_fields(raw_text)

    st.success("✅ Dados extraídos com sucesso!")
    st.markdown("---")
    st.subheader("📋 Dados Identificados:")
    for k, v in fields.items():
        st.write(f"**{k}:** {v if v else 'Não encontrado'}")
