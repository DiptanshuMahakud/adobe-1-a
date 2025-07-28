# PDF Title and Section Classifier

## 🧠 Approach

Our solution combines PDF layout parsing with a fine-tuned NLP model to classify document elements such as titles, section headers (H1, H2, H3), and other non-structural text.

1. **Layout Extraction**:  
   We use `PyMuPDF` (also known as `fitz`) to extract text content along with their positional layout information from the input PDFs.

2. **Text Classification**:  
   A fine-tuned transformer model `all-MiniLM-L12-v2` is used to classify each line of text into one of three categories:
   - Title
   - Section header (H1, H2, H3)
   - Negative (non-title/non-section text)

3. **Post-Processing Heuristics**:  
   After classification, rule-based heuristics refine the results by analyzing font size, indentation, and structural patterns to distinguish between H1, H2, and H3.

---

## 📦 Models and Libraries Used

- **Model**:
  - [`all-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) – fine-tuned for sentence-level classification

- **Python Libraries**:
  - `PyMuPDF` – for PDF parsing and layout information
  - `transformers` – for loading and running the MiniLM model
  - `scikit-learn`, `numpy`, `pandas` – for data manipulation and preprocessing

---

## ⚙️ Build and Run Instructions

### 🏗️ Build Docker Image

Run the following command in the project directory to build the Docker image:

```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
```