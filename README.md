In one terminal, execute::

  llama-server -hf unsloth/gemma-4-E2B-it-GGUF:Q4_K_M --ctx-size 65536

In the other terminal in this directory, execute::

  pi --model unsloth/gemma-4-E2B-it-GGUF:Q4_K_M --tools read,ls,bash -p "turn on the lights, please"

