# coding=utf-8
import os
import sys
import pyperclip

def options(op):
	operSist = sys.platform
	if operSist == 'win32':
		if op == 1:
			return os.system('cls')
		elif op == 2:
			return os.system('pause>nul')
	elif operSist == 'linux' or operSist == 'linux2':
		if op == 1:
			return os.system('clear')
		elif op == 2:
			return os.system('read -p ""')
	else:
		return '¡No se reconoce el sistema operativo!'
		exit()

def cifrar(frase, clave):

	alfa = "abcdefghijklmnñopqrstuvwxyz"
	lista, lista2 = [], []
	
	if frase.__contains__(" "):
		lista = frase.split(" ")
	else:
		lista.append(frase)

	for palabra in lista:
		letCif = ''
		for letra in palabra:
			posicion = alfa.index(letra) + clave
			if posicion > 26:
				nuevaPos = posicion - 27
				letCif += alfa[nuevaPos]
			else:
				letCif += alfa[posicion]
		lista2.append(letCif)

	return lista2


def descifrar(frase, clave):

	alfa = "abcdefghijklmnñopqrstuvwxyz"
	lista, lista2 = [], []
	
	if frase.__contains__(" "):
		lista = frase.split(" ")
	else:
		lista.append(frase)

	for palabra in lista:
		letCif = ''
		for letra in palabra:
			posicion = alfa.index(letra) - clave
			if posicion < 0:
				nuevaPos = posicion + 27
				letCif += alfa[nuevaPos]
			else:
				letCif += alfa[posicion]
		lista2.append(letCif)

	return lista2


def bruteForce(frase):

	lista = []
	
	for clave in range(27):
		lista.append(descifrar(frase, clave))

	return lista


def menu():
	
	options(1)
	print('\n1) Cifrar')
	print('2) Descifrar')
	print('3) Fuerza Bruta')
	print('4) Salir')
	op = input('\nElija una opción: ')

	if op == '1':
		options(1)

		frase = input("\nAgrega una frase: ")
		clave = int(input("Agregar clave de cifrado: "))

		fraseCifrada = cifrar(frase, clave)
		fraseFinal = ''.join(fraseCifrada)
		print('\n' + fraseFinal)
		pyperclip.copy(fraseFinal)
		print('\nLa frase ha sido copiada al portapapeles!')
		
	elif op == '2':
		options(1)

		frase = input("\nInserte mensaje cifrado: ")
		clave = int(input("Agregue clave de descifrado: \n"))

		fraseDescifrada = descifrar(frase, clave)

		print('\nFrase Descifrada: ', end = '')
		for p in fraseDescifrada:
			print(p, end = ' ')

	elif op == '3':
		todas = []
		frase = input("\nInserte mensaje cifrado: ")
		todas = bruteForce(frase)
		for mensaje in todas:
			print(mensaje)

	elif op == '4':
		options(1)
		exit()

	else:
		print('\nPor favor, escoja una opción válida!')
		options(2)
		options(1)
		menu()


menu()
