## Installation

### 1. Fork the Repository

Fork this repository to your GitHub account by clicking the **Fork** button.

### 2. Clone the Repository

Clone your fork to your local machine.

```bash
git clone https://github.com/<niteshver>/NexaSearch.git
```

### 3. Navigate to the Project Directory

```bash
cd NexaSearch
```

### 4. Create a Virtual Environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 5. Install Dependencies

using **uv**:

```bash
uv sync
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and add the required configuration.

```env
# Example
OPENAI_API_KEY=your_api_key
```

### 7. Run the Project

```bash
example
```

> **Note:** The run command may change as the project evolves.