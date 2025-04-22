# 📄 Extrator de Dados de Precatórios - CREAR

Este aplicativo web foi criado para automatizar a leitura de ofícios de precatórios (PDF ou JPG) e extrair automaticamente os dados necessários para alimentar plataformas de cotação.

## 🚀 Funcionalidades

- Upload de arquivos em PDF ou imagem (JPG/PNG)
- Leitura via OCR com Tesseract
- Extração automática dos campos:
  - CPF/CNPJ
  - Requerente
  - Requerido
  - Natureza
  - Vara
  - Estado e Cidade
  - Datas (base e expedição)
  - Número do processo e precatório
  - Descontos e meses de RRA
- Visualização limpa e direta no navegador

## 🖼️ Interface com a marca

Inclui o logotipo da [CREAR](https://crearativos.com.br) no topo para manter a identidade da empresa.

## 🌐 Deploy com Streamlit Cloud

1. Crie uma conta gratuita em: https://streamlit.io/cloud
2. Crie um repositório no GitHub e envie os seguintes arquivos:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. No painel do Streamlit Cloud, clique em **New App**, selecione seu repositório e o arquivo `app.py`
4. Seu app estará online em minutos.

## 🧠 Requisitos locais (opcional)

Caso queira rodar localmente:

```bash
pip install -r requirements.txt
```

Além disso, instale o Tesseract OCR:

- **Windows**: https://github.com/UB-Mannheim/tesseract/wiki
- **Mac**: `brew install tesseract`
- **Linux**: `sudo apt install tesseract-ocr`

Depois rode:

```bash
streamlit run app.py
```

---

### 📬 Contato

Este projeto é mantido pela equipe da [Crear](https://crearativos.com.br). Dúvidas ou melhorias? Entre em contato pelo e-mail: contato@crear.com.br
