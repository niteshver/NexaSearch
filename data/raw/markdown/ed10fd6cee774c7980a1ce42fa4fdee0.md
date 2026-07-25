![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face⟨1⟩
  *  Models ⟨2⟩
  *  Datasets ⟨3⟩
  *  Spaces ⟨4⟩
  *  Buckets new⟨5⟩
  *  Docs ⟨6⟩
  *  Enterprise ⟨7⟩
  * Pricing⟨8⟩
  *     * Website
      *  Tasks⟨9⟩
      *  HuggingChat⟨10⟩
      *  Collections⟨11⟩
      *  Languages⟨12⟩
      *  Organizations⟨13⟩
    * Community
      *  Blog⟨14⟩
      *  Posts⟨15⟩
      *  Daily Papers⟨16⟩
      *  Hardware⟨17⟩
      *  Learn⟨18⟩
      *  Discord⟨19⟩
      *  Forum⟨20⟩
      *  GitHub⟨21⟩
    * Solutions
      *  Team & Enterprise⟨7⟩
      *  Hugging Face PRO⟨22⟩
      *  Enterprise Support⟨23⟩
      *  Inference Providers⟨24⟩
      *  Inference Endpoints⟨25⟩
      *  Storage Buckets⟨5⟩
  * * * *
  * Log In⟨26⟩
  * Sign Up⟨27⟩


# 
 ![](https://huggingface.co/avatars/f1c61308d7013966e978c25c44cf4829.svg) ⟨28⟩
Nitishsharma9⟨28⟩
/
super-lite-model-upload⟨29⟩
like 4
 GGUF ⟨30⟩ qwen ⟨31⟩ cybersecurity ⟨32⟩ ethical-hacking ⟨33⟩ coding ⟨34⟩ 4bit ⟨35⟩ conversational ⟨36⟩
License: apache-2.0
 Model card ⟨29⟩ Files Files and versions xet ⟨37⟩ Community ⟨38⟩
Deploy
Copy to bucket new
Use this model
### Instructions to use Nitishsharma9/super-lite-model-upload with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  *  llama-cpp-python⟨39⟩
How to use Nitishsharma9/super-lite-model-upload with llama-cpp-python:

```
# !pip install llama-cpp-python

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="Nitishsharma9/super-lite-model-upload",
	filename="super-lite-cyber-coder-q4_k_m.gguf",
)

```

```
llm.create_chat_completion(
	messages = "No input example has been defined for this model task."
)
```

  * Notebooks
  *  Google Colab⟨40⟩
  *  Kaggle⟨41⟩
  * Local Apps Settings⟨42⟩
  *  llama.cpp ⟨43⟩
How to use Nitishsharma9/super-lite-model-upload with llama.cpp:
##### Install (macOS, Linux)

```
curl -LsSf https://llama.app/install.sh | sh
# Start a local OpenAI-compatible server with a web UI:
llama serve -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
# Run inference directly in the terminal:
llama cli -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Install from WinGet (Windows)

```
winget install llama.cpp
# Start a local OpenAI-compatible server with a web UI:
llama serve -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
# Run inference directly in the terminal:
llama cli -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Use pre-built binary

```
# Download pre-built binary from:
# https://github.com/ggerganov/llama.cpp/releases
# Start a local OpenAI-compatible server with a web UI:
./llama-server -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
# Run inference directly in the terminal:
./llama-cli -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Build from source code

```
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
cmake -B build
cmake --build build -j --target llama-server llama-cli
# Start a local OpenAI-compatible server with a web UI:
./build/bin/llama-server -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
# Run inference directly in the terminal:
./build/bin/llama-cli -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Use Docker

```
docker model run hf.co/Nitishsharma9/super-lite-model-upload:Q4_K_M
```

  *  LM Studio ⟨44⟩
  *  Jan ⟨45⟩
  *  Ollama ⟨46⟩
How to use Nitishsharma9/super-lite-model-upload with Ollama:

```
ollama run hf.co/Nitishsharma9/super-lite-model-upload:Q4_K_M
```

  *  Unsloth Studio ⟨47⟩
How to use Nitishsharma9/super-lite-model-upload with Unsloth Studio:
##### Install Unsloth Studio (macOS, Linux, WSL)

```
curl -fsSL https://unsloth.ai/install.sh | sh
# Run unsloth studio
unsloth studio -H 0.0.0.0 -p 8888
# Then open http://localhost:8888 in your browser
# Search for Nitishsharma9/super-lite-model-upload to start chatting
```

##### Install Unsloth Studio (Windows)

```
irm https://unsloth.ai/install.ps1 | iex
# Run unsloth studio
unsloth studio -H 0.0.0.0 -p 8888
# Then open http://localhost:8888 in your browser
# Search for Nitishsharma9/super-lite-model-upload to start chatting
```

##### Using HuggingFace Spaces for Unsloth

```
# No setup required
# Open https://huggingface.co/spaces/unsloth/studio in your browser
# Search for Nitishsharma9/super-lite-model-upload to start chatting
```

  *  Pi ⟨48⟩
How to use Nitishsharma9/super-lite-model-upload with Pi:
##### Start the llama.cpp server

```
# Install llama.cpp:
brew install llama.cpp
# Start a local OpenAI-compatible server:
llama serve -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Configure the model in Pi

```
# Install Pi:
npm install -g @mariozechner/pi-coding-agent
# Add to ~/.pi/agent/models.json:
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "none",
      "models": [
        {
          "id": "Nitishsharma9/super-lite-model-upload:Q4_K_M"
        }
      ]
    }
  }
}
```

##### Run Pi

```
# Start Pi in your project directory:
pi
```

  *  Hermes Agent new⟨49⟩
How to use Nitishsharma9/super-lite-model-upload with Hermes Agent:
##### Start the llama.cpp server

```
# Install llama.cpp:
brew install llama.cpp
# Start a local OpenAI-compatible server:
llama serve -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Configure Hermes

```
# Install Hermes:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup
# Point Hermes at the local server:
hermes config set model.provider custom
hermes config set model.base_url http://127.0.0.1:8080/v1
hermes config set model.default Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Run Hermes

```
hermes
```

  *  Atomic Chat new⟨50⟩
  *  OpenClaw new⟨51⟩
How to use Nitishsharma9/super-lite-model-upload with OpenClaw:
##### Start the llama.cpp server

```
# Install llama.cpp:
brew install llama.cpp
# Start a local OpenAI-compatible server:
llama serve -hf Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Configure OpenClaw

```
# Install OpenClaw:
npm install -g openclaw@latest
# Register the local server and set it as the default model:
openclaw onboard --non-interactive --mode local \
  --auth-choice custom-api-key \
  --custom-base-url http://127.0.0.1:8080/v1 \
  --custom-model-id "Nitishsharma9/super-lite-model-upload:Q4_K_M" \
  --custom-provider-id llama-cpp \
  --custom-compatibility openai \
  --custom-text-input \
  --accept-risk \
  --skip-health
```

##### Run OpenClaw

```
openclaw agent --local --agent main --message "Hello from Hugging Face"
```

  *  Docker Model Runner ⟨52⟩
How to use Nitishsharma9/super-lite-model-upload with Docker Model Runner:

```
docker model run hf.co/Nitishsharma9/super-lite-model-upload:Q4_K_M
```

  *  Lemonade ⟨53⟩
How to use Nitishsharma9/super-lite-model-upload with Lemonade:
##### Pull the model

```
# Download Lemonade from https://lemonade-server.ai/
lemonade pull Nitishsharma9/super-lite-model-upload:Q4_K_M
```

##### Run and chat with the model

```
lemonade run user.super-lite-model-upload-Q4_K_M
```

##### List all available models

```
lemonade list
```



  * Super-Lite Cyber Coder 1.5B (GGUF)⟨54⟩
    * Target Hardware⟨55⟩
    * How to use with PocketPal AI (Mobile)⟨56⟩
    * How to use with LM Studio / Ollama⟨57⟩
    * What this command does:⟨58⟩


#   ⟨54⟩ Super-Lite Cyber Coder 1.5B (GGUF) 
This is a highly optimized, super-lite language model designed for **Clean, secure code generation, debugging, and authorized ethical hacking & penetration testing methodologies.** It has been fine-tuned on coding and cybersecurity datasets, maintaining strict adherence to defensive and educational boundaries.
##   ⟨55⟩ Target Hardware 
  * **RAM Requirement:** < 4GB
  * **Format:** GGUF (Q4_K_M)
  * **Size:** < 1.2 GB
  * **Context Length:** 2048 Tokens


##   ⟨56⟩ How to use with PocketPal AI (Mobile) 
  1. Download PocketPal AI from your device's app store.
  2. Load the `super-lite-cyber-coder-q4_k_m.gguf` file directly into the app.
  3. Configure the chat template to use ChatML (`<|im_start|>` / `<|im_end|>`).
  4. Set the system prompt to enforce safe, authorized penetration testing boundaries.


##   ⟨57⟩ How to use with LM Studio / Ollama 
  * **Ollama:** Since you're on Windows, here’s the exact command to download and run it with Ollama:
  * _ollama run hf.co/Nitishsharma9/super-lite-model-upload:Q4_K_M:_


##   ⟨58⟩ What this command does: 
**ollama run: This tells Ollama to run a model.**
  1. **hf.co/...: This is the special identifier that tells Ollama to look for the model on Hugging Face (hf.co is the short URL for huggingface.co).:**
  2. **Nitishsharma9/super-lite-model-upload: This is the repository path on Hugging Face.:**
  3. **:Q4_K_M: This specifies the exact quantization file (the .gguf file) to use, which matches the file you were trying to use earlier.:**
  4. **When you run this command for the first time, Ollama will automatically download the model file from Hugging Face and store it locally. After the download finishes, you'll be placed directly into an interactive chat session with the model.:**



Downloads last month
    115
GGUF⟨59⟩
Model size
2B params
Architecture
qwen2
Chat template
Hardware compatibility
Log In⟨60⟩ to add your hardware
4-bit
Q4_K_M 986 MB
Inference Providers NEW⟨61⟩
This model isn't deployed by any Inference Provider. 🙋 1 Ask for provider support⟨62⟩
System theme
Company
TOS⟨63⟩ Privacy⟨64⟩ About⟨65⟩ Careers⟨66⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
Inference providers allow you to run inference using different serverless providers.
