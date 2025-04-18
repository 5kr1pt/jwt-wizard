#!/usr/bin/env python3
"""
Ferramenta CLI para:
1. Receber um JWT e a chave secreta
2. Exibir o payload já decodificado
3. Permitir que o usuário edite claims na hora
4. Renovar tempos (iat/nbf/exp) automaticamente
5. Gerar o novo token assinado
"""

import json
import time
import argparse
from getpass import getpass

import jwt


def decode_no_verify(token: str) -> dict:
    """Decodifica sem verificar assinatura/expiração."""
    return jwt.decode(
        token,
        options={
            "verify_signature": False,
            "verify_exp": False,
            "verify_nbf": False,
        },
        algorithms=["HS256", "HS512", "RS256", "none"],
    )


def interactive_edit(payload: dict) -> dict:
    """Loop para alterar/adi‑cionar claims via prompt."""
    print("\n--- Payload atual ---")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    print(
        "\nEdite os claims (ENTER vazio para terminar). "
        "Use 'del <chave>' para remover."
    )
    while True:
        field = input("Campo a alterar: ").strip()
        if not field:
            break
        if field.startswith("del "):
            key = field.split(" ", 1)[1]
            payload.pop(key, None)
            print(f"• '{key}' removido")
            continue
        value = input(f"Novo valor para '{field}': ").strip()
        payload[field] = value
    return payload


def refresh_times(payload: dict, lifetime: int = 3600) -> None:
    """Atualiza iat/nbf/exp."""
    now = int(time.time())
    payload.update({"iat": now, "nbf": now, "exp": now + lifetime})


def generate_token(payload: dict, secret: str, alg: str = "HS256") -> str:
    return jwt.encode(payload, secret, algorithm=alg)


def cli():
    parser = argparse.ArgumentParser(
        description="Wizard para editar e re‑assinar JWTs facilmente."
    )
    parser.add_argument("--token", help="JWT antigo (se não usar modo interativo)")
    parser.add_argument("--secret", help="Chave secreta")
    parser.add_argument(
        "--set",
        metavar="K=V",
        nargs="*",
        help="Altera claims sem prompt (pode repetir). Ex: --set sub=1 role=admin",
    )
    args = parser.parse_args()

    # === Leitura interativa caso flags não sejam usadas =======================
    token = args.token or input("🔒 JWT antigo: ").strip()
    secret = args.secret or getpass("🔑 Chave secreta (entrada oculta): ").strip()

    payload = decode_no_verify(token)

    # Flags --set têm prioridade; se não houver, cai no modo de edição manual
    if args.set:
        for pair in args.set:
            k, _, v = pair.partition("=")
            payload[k] = v
    else:
        payload = interactive_edit(payload)

    refresh_times(payload)

    new_token = generate_token(payload, secret)
    print("\n✅ Novo JWT gerado:\n")
    print(new_token)


if __name__ == "__main__":
    cli()
