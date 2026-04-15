# LiteParse Benchmark: PDF Parsing for LLM Q&A

This project evaluates how different PDF parsing approaches affect Large Language Model (LLM) performance in document question-answering tasks.

Instead of focusing on the model, this experiment highlights how **input quality (text extraction)** impacts results.

---

## 🚀 Overview

We compare three PDF extraction methods:

* **PyPDF** → fast, but flattens text (loses structure)
* **pdfplumber** → partial layout preservation
* **LiteParse** → preserves spatial alignment (ASCII-style text)

All extracted outputs are passed to the same LLM to ensure a fair comparison.

---

## 🧠 Key Idea

> Better input → Better understanding

The LLM is not the bottleneck — the quality of extracted text is.

---

## 🛠️ Tech Stack

* Python
* PyPDF
* pdfplumber
* LiteParse
* Ollama
* Gemma 4 (`gemma4:e4b`)

---

## 📂 Project Structure

```
liteparse-benchmark/
├── parse.py
├── requirements.txt
├── wipo_pub_rn2021_18e.pdf
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/ParthSingh0506/learn-lite-parse.git
cd liteparse-benchmark
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and run Ollama

Download from: [https://ollama.com](https://ollama.com)

Pull the model:

```bash
ollama pull gemma4:e4b
```

---

## ▶️ Run the Experiment

```bash
python parse.py
```

---

## 🧪 What the Script Does

Pipeline:

```
PDF → Text Extraction → LLM → Answer
```

Steps:

1. Extract text using each method
2. Send extracted text to the LLM
3. Ask the same question
4. Measure:

   * Parsing time
   * Inference time

---

## 📊 Example Output

| Method     | Parse Time | Inference Time |
| ---------- | ---------- | -------------- |
| PyPDF      | ~0.08s     | ~22s           |
| pdfplumber | ~0.38s     | ~2.5s          |
| LiteParse  | ~0.74s     | ~24s           |

---

## 🔍 Observations

* All methods can return correct answers in simple cases
* PyPDF loses structure → can confuse LLMs
* pdfplumber works for simpler layouts
* LiteParse preserves alignment → more reliable understanding

---

## ⚠️ Important Note

LiteParse may increase:

* parsing time (slightly)
* inference time (due to more tokens)

But it improves:

* input clarity
* structural consistency

---

## 💡 When to Use LiteParse

* Financial reports
* Tables in PDFs
* Multi-column documents
* Structured layouts without markup

---

## ❌ Limitations

LiteParse does not:

* detect tables explicitly
* output structured formats (CSV/JSON)
* understand semantics

It only preserves layout.

---

## 🏁 Conclusion

> Don’t optimize your model first.
> Fix your input.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests.

---

## ⭐ Support

If you found this useful, consider giving the repo a star!
