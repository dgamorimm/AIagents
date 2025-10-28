{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "client = openai.Client()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fluxo de Conversa\n",
    "- User: Usuário que inicia a conversa\n",
    "- Assistant: Bot que responde a pergunta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "mensagens = [{\"role\":\"user\", \"content\":\"Defina uma laranja em 5 palavras\"}]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "resposta = client.chat.completions.create(\n",
    "    messages=mensagens,\n",
    "    model=\"gpt-3.5-turbo-0125\",\n",
    "    max_tokens=1000,\n",
    "    temperature=0\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ChatCompletion(id='chatcmpl-ApxWt4R2qrgHUMPS7Icvj2EDlJcn0', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Fruta cítrica suculenta e saborosa.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1736946923, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=15, prompt_tokens=18, total_tokens=33, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resposta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Fruta cítrica suculenta e saborosa.'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resposta.choices[0].message.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "mensagens.append({\"role\":\"assistant\", \"content\":resposta.choices[0].message.content})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "mensagens.append({\"role\":\"user\", \"content\":\"E qual a sua cor?\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "resposta = client.chat.completions.create(\n",
    "    messages=mensagens,\n",
    "    model=\"gpt-3.5-turbo-0125\",\n",
    "    max_tokens=1000,\n",
    "    temperature=0\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Laranja.'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resposta.choices[0].message.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "mensagens.append({\"role\":\"assistant\", \"content\":resposta.choices[0].message.content})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'role': 'user', 'content': 'Defina uma laranja em 5 palavras'},\n",
       " {'role': 'assistant', 'content': 'Fruta cítrica suculenta e saborosa.'},\n",
       " {'role': 'user', 'content': 'E qual a sua cor?'},\n",
       " {'role': 'assistant', 'content': 'Laranja.'}]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mensagens"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Utilizando Função"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def geracao_texto(mensagens, model=\"gpt-3.5-turbo-0125\", max_tokens=1000, temperature=0):\n",
    "    resposta = client.chat.completions.create(\n",
    "        messages=mensagens,\n",
    "        model=model,\n",
    "        max_tokens=max_tokens,\n",
    "        temperature=temperature\n",
    "    )\n",
    "    mensagens.append({\"role\":\"assistant\", \"content\":resposta.choices[0].message.content})\n",
    "    return mensagens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "msg1 = [{\"role\":\"user\", \"content\": \"Defina o que é API em 5 palavras\"}]\n",
    "mensagens = geracao_texto(msg1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'role': 'user', 'content': 'Defina o que é API em 5 palavras'},\n",
       " {'role': 'assistant', 'content': 'Interface de programação de aplicativos.'}]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mensagens"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Utilizando Stream"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "mensagens = [{\"role\":\"user\", \"content\":\"Conte uma história simples e objetiva sobre LLM\"}]\n",
    "resposta = client.chat.completions.create(\n",
    "        messages=mensagens,\n",
    "        model=\"gpt-3.5-turbo-0125\",\n",
    "        max_tokens=1000,\n",
    "        temperature=0,\n",
    "        stream=True\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<openai.Stream at 0x1459b69de10>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resposta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LLM era um jovem estudante de direito muito dedicado e determinado. Desde pequeno, ele sonhava em se tornar um advogado renomado e ajudar as pessoas a obter justiça.\n",
      "\n",
      "Durante seus estudos, LLM se destacava pela sua inteligência e capacidade de argumentação. Ele sempre se esforçava ao máximo para aprender e se aprimorar, buscando sempre novos desafios e oportunidades de crescimento.\n",
      "\n",
      "Após se formar, LLM conseguiu um emprego em um escritório de advocacia de prestígio, onde rapidamente se destacou pelo seu trabalho árduo e dedicação aos clientes. Sua reputação como advogado competente e ético logo se espalhou, e ele passou a ser procurado por pessoas de todo o país em busca de sua ajuda.\n",
      "\n",
      "Com o passar dos anos, LLM se tornou um dos advogados mais respeitados do país, conhecido por sua integridade, competência e comprometimento com a justiça. Ele nunca se deixou levar pelo dinheiro ou pela fama, sempre colocando o bem-estar de seus clientes em primeiro lugar.\n",
      "\n",
      "LLM continuou sua carreira brilhante por muitos anos, sempre lutando pelos direitos daqueles que precisavam de sua ajuda. Sua história se tornou um exemplo de determinação, ética e sucesso na advocacia, inspirando gerações futuras de advogados a seguirem seus passos."
     ]
    }
   ],
   "source": [
    "for resposta_stream in resposta:\n",
    "    texto = resposta_stream.choices[0].delta.content\n",
    "    if texto:\n",
    "        print(texto, end=\"\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
