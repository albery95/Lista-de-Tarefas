#!/usr/bin/env python3
#
#  teste.py
#  
#  Copyright 2026 albery <albery@albery-notebook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import os
import json

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
	# Verifica se o arquivo existe antes de tentar abrir
	if os.path.exists(ARQUIVO_TAREFAS):
		with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
			return json.load(f)
	return []
def salvar_tarefas(tarefas):
	with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
		json.dump(tarefas, f, indent=4, ensure_ascii=False)

def exibir_menu():
	print("\n--- Gerenciador de memoria ---")
	print("1. Adicionar Tarefa")
	print("2. Listar Tarefas")
	print("3. Remover Tarefas")
	print("4. Sair")
	
def main():
	tarefas = carregar_tarefas() #Carrega os dados ao abrir
	
	while True:
		exibir_menu()
		escolha = input("\nEscolha: ")
		
		if escolha == '1':
			nova = input("Descrição: ")
			tarefas.append(nova)
			salvar_tarefas(tarefas) # Salvar a mudança
			print("Salvo!")
		
		elif escolha == '2':
			print("\nTarefas: ")
			for i, t in enumerate(tarefas, 1):
				print(f"{i}. {t}")
		
		elif escolha == '3':
			try:
				num = int(input("Número para remover: "))
				tarefas.pop(num - 1)
				salvar_tarefas(tarefas) #Salva a mudança
				print("Removido!")
			except:
				print("Erro ao remover.")
		
		elif escolha == '4':
			print("Tchau!")
			break 

if __name__ == "__main__":
	main()



