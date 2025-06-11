Claro! Aqui está uma versão aprimorada do seu README com uma estrutura mais clara, correção de pequenos erros e explicações mais precisas. Mantive o conteúdo técnico e o estilo direto, sem emojis:

---

# Comandos Linux — Trabalho G2

Este documento apresenta exemplos de uso de comandos Linux utilizados na criação, edição, permissões e transferência de arquivos e diretórios.

---

## `mkdir` — Criar diretórios

Cria pastas no sistema de arquivos.

```bash
mkdir ~/trabalho
mkdir ~/trabalho/relatorios
mkdir ~/trabalho/documentos
```

---

## `touch` — Criar arquivos vazios

Cria arquivos em branco.

```bash
touch ~/trabalho/relatorios/relatorio.txt
touch ~/trabalho/documentos/notas.txt
```

---

## `nano` — Editar arquivos no terminal

Abre o editor de texto `nano` para inserir ou modificar o conteúdo dos arquivos.

```bash
nano ~/trabalho/relatorios/relatorio.txt
```

Conteúdo inserido:

```
Relatório de Trabalho
Data: 07/05/2025
```

```bash
nano ~/trabalho/documentos/notas.txt
```

Conteúdo inserido:

```
Notas Finais:
- Estudo de caso: 85
- Performance: 90
```

---

## `chmod` — Alterar permissões de arquivos

Define permissões de leitura, escrita e execução.

```bash
chmod 644 ~/trabalho/relatorios/relatorio.txt   # Leitura e escrita para o dono; leitura para os outros
chmod 700 ~/trabalho/documentos/notas.txt       # Acesso total apenas para o dono
```

---

## `ls -la` — Listar arquivos com detalhes

Exibe informações detalhadas sobre arquivos e permissões.

```bash
ls -la ~/trabalho/relatorios/relatorio.txt
ls -la ~/trabalho/documentos/notas.txt
```

---

## `scp` — Transferir arquivos entre máquinas (via SSH)

Permite copiar arquivos de/para outra máquina através do protocolo seguro.

```bash
# Enviar arquivo local para o servidor
scp C:\Users\1135300\Downloads\arquivo_local.txt RICHARD@191.252.109.103:~/trabalho/

# Baixar arquivo do servidor para o computador local
scp RICHARD@191.252.109.103:~/trabalho/documentos/notas.txt C:\Users\1135300\Downloads\
```

---

Se quiser, posso incluir uma introdução ou conclusão explicando o contexto do trabalho. Deseja isso?
