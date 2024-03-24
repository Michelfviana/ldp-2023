def get_answer():
	valid_responses = ("sim", "não")
	while True:
		response = input("Você me ama? (sim/não): ").lower()
		if response in valid_responses:
			return response
		else:
			print(
				"Desculpe, resposta inválida. Por favor, responda com 'sim' ou 'não'."
			)


def main():
	answer = get_answer()
	if answer == "sim":
		print("Que bom! Eu também te adoro!")
	elif answer == "não":
		print("Ah, que pena! Estou aqui se precisar de mim.")


if __name__ == "__main__":
	main()
