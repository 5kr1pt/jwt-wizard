# 🔐 JWT‑Wizard

CLI super enxuta para decodificar, editar e re‑assinar JSON Web Tokens **sem sofrimento** e sem depender do jwt.io kkkkkk.

---

## Instalação

```bash
git clone https://github.com/5kr1pt/jwt-wizard.git
cd jwt‑wizard
python -m venv .venv && source .venv/bin/activate ```ou conforme o seu shell```
pip install -r requirements.txt
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
    

### 📽️ 🇧🇷 Como instalar:

![Demonstração CLI](docs/demo.mp4)


---

## Licença

MIT © 2025 Paulo Galino Werneck


### .gitignore mínimo`

.venv/ **pycache**/ *.pyc
