# Comandos linux trabalho G2

## `mkdir`: Cria diretórios no sistema de arquivos

⁠ bash
mkdir ~/trabalho
mkdir ~/trabalho/relatorios
mkdir ~/trabalho/documentos
 ⁠

## `touch`: Cria arquivos vazios
⁠ bash
touch ~/trabalho/relatorios/relatorio.txt
touch ~/trabalho/documentos/notas.txt
 ⁠

## `nano`: Escrita em arquvios
⁠ bash
nano ~/trabalho/relatorios/relatorio.txt -> (inseridas linhas abaixo no arquivo)
Relatório de Trabalho
Data: 07/05/2025
 
nano ~/trabalho/documentos/notas.txt -> (inseridas linhas abaixo no arquivo)
Notas Finais:
- Estudo de caso: 85
- Performance: 90

## `chmod`: Alterar permissões
⁠ bash
chmod 644 ~/trabalho/relatorios/relatorio.txt
chmod 700 ~/trabalho/documentos/notas.txt
 ⁠

## `ls -la`: Listar arquivos
⁠ bash
ls -la ~/trabalho/relatorios/relatorio.txt
ls -la ~/trabalho/documentos/notas.txt
 ⁠

## `scp`: Transferir arquivos entre máquinas
⁠ bash
scp C:\Users\1135300\Downloads\arquivo_local.txt RICHARD@191.252.109.103:~/trabalho/
scp RICHARD@191.252.109.103:~/trabalho/documentos/notas.txt C:\Users\1135300\Downloads\
