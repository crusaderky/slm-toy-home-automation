In one terminal, execute::

  llama-server -hf lm-kit/qwen-3-1.7b-instruct-gguf:Q4_K_M --ctx-size 1024

In the other terminal in this directory, execute::

  pi --model lm-kit/qwen-3-1.7b-instruct-gguf:Q4_K_M --tools "" -p "turn on the lights, please"

