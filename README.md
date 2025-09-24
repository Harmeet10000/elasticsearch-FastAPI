# 🔍 Elasticsearch Python Tutorial

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.x-yellow.svg)](https://www.elastic.co/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

A comprehensive tutorial repository for mastering Elasticsearch with Python. This hands-on course covers everything from basic search operations to advanced semantic search using vector embeddings.

## 🎯 What I  Learnt

This course provided by freecodecamp gives practical experience with key Elasticsearch concepts:

- 🔎 **Regular Search** - Multi-field queries with pagination and filtering
- 📝 **N-gram Tokenization** - Advanced text analysis for better search results
- 🧠 **Semantic Search** - Vector embeddings for contextual understanding
- 📊 **Aggregations** - Data analytics and statistical operations
- 🎯 **KNN Search** - Similarity matching with embeddings
- 🔄 **Data Ingest Pipelines** - Automated data processing workflows

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Elasticsearch 8.x
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harmeet10000/elasticsearch-FastAPI.git
   cd elasticsearch-FastAPI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Elasticsearch**
   ```bash
   docker run -d --name elasticsearch \
     -p 9200:9200 -p 9300:9300 \
     -e "discovery.type=single-node" \
     elasticsearch:8.11.0
   ```

4. **Run the final project**
   ```bash
   cd final_project/backend
   uvicorn main:app --reload
   ```

## 🛠️ Technologies Used

- **Backend**: FastAPI, Python
- **Search Engine**: Elasticsearch
- **ML Models**: Sentence Transformers
- **Frontend**: Vue
- **Data Processing**: Pandas, NumPy

## 📚 Learning Path

1. **Fundamentals** - Start with basic Elasticsearch concepts
2. **Search Operations** - Learn querying and filtering
3. **Text Analysis** - Explore tokenization and analyzers
4. **Vector Search** - Implement semantic search with embeddings
5. **Analytics** - Master aggregations and data insights
6. **Final Project** - Build a complete search application

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs or issues
- Suggest new features or improvements
- Submit pull requests
- Share feedback and experiences

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Acknowledgments

Special thanks to the Elasticsearch and Python communities for their excellent documentation and resources.

---

**Happy learning!** 🚀 Dive into the world of modern search with Elasticsearch and Python.
