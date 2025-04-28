# 🔐 JWT‑Wizard

## ⚠️ Aviso de Segurança

Este programa **desativa** todas as verificações de segurança padrão de um JWT:

- Desliga a verificação de assinatura (`verify_signature=False`)
- Ignora checagens de expiração (`verify_exp=False`) e “not before” (`verify_nbf=False`)
- Permite o uso do algoritmo `"none"` sem qualquer assinatura

**IMPORTANTE:**  
Este script destina‑se **exclusivamente** a fins educacionais, testes em laboratório ou CTFs.  
**NÃO USE** este código em ambientes de produção ou sempre que a integridade/autenticidade dos tokens for crítica — você estará exposto a ataques de falsificação de JWT e outras vulnerabilidades graves.

Esse programa é uma CLI super enxuta para decodificar, editar e re‑assinar JSON Web Tokens **sem sofrimento**.

---

## Instalação

```bash
git clone https://github.com/5kr1pt/jwt-wizard.git
cd jwt‑wizard/
python -m venv .venv && source .venv/bin/activate ```ou conforme o seu shell```
pip install -r requirements.txt
cd jwt-wizard/
python3 ./cli.py ou python ./cli.py
```

⚡️ Apenas Python 3.8+ e `PyJWT` como dependência de runtime.

## Uso Rápido

`python -m jwt_wizard          # modo 100 % interativo`

### Exemplos avançados

|cenário|comando|
|---|---|
|Editar via prompt|`python -m jwt_wizard`|
|Alterar claims sem prompt|`python -m jwt_wizard --token "$OLD" --secret "$KEY" --set sub=1 role=admin`|
|Encadear num script|`NEW=$(python -m jwt_wizard --token "$OLD" --secret "$KEY" --set exp=$(($(date +%s)+7200)))`|

---

## Principais Features

- **Decodificação segura** (ignora assinatura/expiração só durante edição)
    
- **Prompt interativo** para adicionar, alterar ou remover claims
    
- **Renovação automática** de `iat`, `nbf` e `exp` (default = +1 h)
    
- **Modo batch** via flags (`--set K=V`) para automação
    
- Compatível com HS256/HS512/RS256/none (decodificação)
    
---

### 📽️ 🇧🇷 Como instalar - Video:

[![Demonstração do JWT Wizard](https://img.youtube.com/vi/m4_HoBReFkI/hqdefault.jpg)](https://youtu.be/m4_HoBReFkI?si=wJUPdc_EIpRdksNU)


<!-- ### 📽️ 🇺🇸 How to install - Video: -->


---

## 📄 Licença

Este projeto está licenciado sob a Licença [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
